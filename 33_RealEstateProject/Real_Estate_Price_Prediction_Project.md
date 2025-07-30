# Real Estate Price Prediction Project: A Comprehensive Machine Learning Pipeline

This document provides a detailed explanation of a real estate price prediction machine learning project, covering data loading, extensive cleaning and preprocessing, outlier treatment, feature engineering, model training and evaluation using linear regression, and preparation for model deployment. The content is derived entirely from the `real_estate_project.py` script.

## 1. Project Goal and Initial Data Loading

* **Goal:** The primary objective is to build a predictive model capable of estimating the price of a property based on its various characteristics and features.
* **Data Loading:** The project uses the `Bengaluru_House_Data.csv` dataset.
    ```python
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    df = pd.read_csv('[https://github.com/bipulshahi/Dataset/raw/refs/heads/main/Bengaluru_House_Data.csv](https://github.com/bipulshahi/Dataset/raw/refs/heads/main/Bengaluru_House_Data.csv)')
    df.head()
    ```
* **Initial Data Inspection:** Basic DataFrame methods are used to get an overview of the data.
    * `df.shape`: Returns the dimensions (rows, columns) of the DataFrame.
    * `df.dtypes`: Shows the data type of each column.
    * `df.nunique()`: Counts unique values in each column.
    * `df.isna().sum()`: Sums the number of missing (NaN) values per column.

## 2. Data Cleaning and Preprocessing

This is a crucial phase to handle inconsistencies, missing values, and transform data into a usable format. A copy of the original DataFrame (`df1 = df.copy()`) is made to preserve the raw data.

* **`area_type` Column Cleaning:**
    * All text in `area_type` is converted to lowercase and leading/trailing spaces are removed (`.str.lower()`, `.str.strip()`).
    * A specific typo "super built-up area " is corrected to "super built-up area".
    * All other `area_type` categories are binned into an 'Others' category for simplification.
    ```python
    df1['area_type'] = df1['area_type'].str.lower()
    df1['area_type'] = df1['area_type'].str.strip()
    df1['area_type'] = df1['area_type'].apply(lambda x : "super built-up area" if x == "super built-up  area" else 'Others')
    df1['area_type'].value_counts()
    ```
* **`availability` Column Cleaning:**
    * The `availability` column's unique values are inspected (`.unique()`, `.value_counts()`).
    * All availability statuses other than "Ready To Move" are standardized to "UC" (Under Construction).
    ```python
    df1['availability'] = df1['availability'].apply(lambda x : "UC" if x != "Ready To Move" else x)
    df1['availability'].value_counts()
    ```
* **`location` Column Cleaning:**
    * Location names are converted to lowercase and stripped of extra spaces.
    * **Handling Low-Frequency Locations:** Locations with fewer than 30 data samples (`location_count < 30`) are identified and grouped into a general category (effectively filtered out in `df2`). This helps manage high cardinality and reduces noise from rare locations.
    ```python
    df1['location'] = df1['location'].str.lower()
    df1['location'] = df1['location'].str.strip()
    location_count = df1['location'].value_counts()
    less_count_location = location_count[location_count < 30].index.to_list()
    # Filter data for locations with at least 30 samples:
    df2 = df1[df1['location'].apply(lambda name_of_location: name_of_location not in less_count_location)]
    df2['location'].value_counts()
    ```
* **`size` Column Cleaning (BHK/Bedroom):**
    * The `size` column, which indicates BHK (Bedroom, Hall, Kitchen) or Bedroom count, is inspected for unique values.
    * A function `fix_size` extracts the numerical part from strings like "2 BHK" or "4 Bedroom". It handles non-standard formats by returning `np.nan`.
    ```python
    def fix_size(size):
      try:
        return int(size.split(' ')[0]) # Extracts integer from "2 BHK"
      except:
        return size # Returns original if conversion fails
    df2['size'] = df2['size'].apply(fix_size)
    ```
    * Properties with `size` greater than 6 are filtered out, as they might be outliers or represent different property types (e.g., commercial).
    ```python
    df5 = df2[~(df2['size'] > 6)]
    df5['size'].value_counts()
    ```
* **`society` Column Handling:**
    * The `society` column is checked for missing values (`.isna().sum()`) and their proportion (`.isna().sum()/len(df2)`).
    * Due to a high percentage of missing values (implied by typical real estate datasets; the code doesn't print the percentage, but drops the column), the `society` column is dropped.
    ```python
    df3 = df2.drop(columns = 'society')
    ```
* **Handling Remaining Missing Values (`dropna`)**:
    * Rows with `NaN` values in the `location` column are dropped, as `location` is a critical feature.
    ```python
    df4 = df3.dropna(subset=['location'])
    ```
* **`total_sqft` Column Cleaning:**
    * The `total_sqft` column contains numerical values and ranges (e.g., "2100 - 2850").
    * A `fix_total_sqft` function is defined:
        * If the area is already a float, it's returned as is.
        * If it's a range (e.g., "2100 - 2850"), it calculates the average of the range.
        * For any other format, it returns `np.nan`.
    ```python
    def fix_total_sqft(area):
      try:
        return float(area)
      except:
        try:
          return (int(area.split('-')[0]) + int(area.split('-')[1]))/2
        except:
          return np.nan
    df5['total_sqft'] = df5['total_sqft'].apply(fix_total_sqft)
    ```
    * **Imputation for Missing `total_sqft`:**
        * The mean `total_sqft` is calculated for each `size` (BHK) group.
        * Missing `total_sqft` values are then filled using the mean `total_sqft` corresponding to their `size`.
        ```python
        size_sqft = df5.groupby('size')['total_sqft'].mean()
        df5['total_sqft'] = df5['total_sqft'].fillna(df5['size'].apply(lambda s: size_sqft.get(s, np.nan)))
        ```
    * **Imputation for Missing `size` (if any still exist):**
        * A `fix_size` function is defined to infer `size` based on `total_sqft` ranges (e.g., <1000 sqft -> size 1, <1500 sqft -> size 2, etc.).
        * Missing `size` values are filled using this function.
        ```python
        def fix_size(sqft):
          if sqft < 1000: return 1
          elif sqft < 1500: return 2
          elif sqft < 2000: return 3
          elif sqft < 2500: return 4
          elif sqft < 3000: return 5
          else: return 6
        df5['size'] = df5['size'].fillna(df5['total_sqft'].apply(fix_size))
        ```
* **`bath` Column Cleaning:**
    * Missing `bath` values are filled using a simple heuristic: `bath = size + 1`. This assumes properties with more bedrooms typically have more bathrooms.
    ```python
    df5['bath'] = df5['bath'].fillna(df5['size'] + 1)
    df5['bath'].unique()
    df5['bath'].value_counts()
    ```
* **`balcony` Column Cleaning:**
    * A crosstabulation (`pd.crosstab(df5['size'] , df['balcony'])`) is performed to understand the relationship between `size` and `balcony`.
    * Missing `balcony` values are filled based on `size`: 1 balcony if `size <= 2`, otherwise 2 balconies.
    ```python
    df5['balcony'] = df5['balcony'].fillna(df5['size'].apply(lambda x : 1 if x <= 2 else 2))
    ```
* **Final Missing Value Check:** After all cleaning steps, `df5.isna().sum()` is run again to confirm no missing values remain.

## 3. Outlier Treatment

Outliers are extreme values that can disproportionately affect model training. This section focuses on identifying and handling them, especially at a granular (per-location) level.

* **Initial Visual Inspection:** Box plots are used to visualize the distribution of `total_sqft`, `price`, and `PPS` (Price Per Square Foot) to identify potential outliers.
    ```python
    plt.subplot(1,2,1)
    df5['total_sqft'].plot.box() # Box plot for total_sqft
    plt.subplot(1,2,2)
    df5['price'].plot.box()     # Box plot for price
    plt.show()

    import seaborn as sns
    plt.figure(figsize = (30,5))
    sns.boxplot(x = df5['location'] , y = df5['total_sqft']) # Box plot of total_sqft per location
    plt.xticks(rotation = 90)
    plt.show()
    ```
* **Price Per Square Foot (PPS) Calculation:** A new feature, `PPS`, is calculated as `(price * 100000) / total_sqft`. This helps in normalizing price by area, making outliers easier to spot.
    ```python
    df5['PPS'] = (df5['price']*100000)/df5['total_sqft']
    ```
    `PPS` is also visualized with box plots per location.

* **Outlier Removal (Clipping using IQR - Per Group):**
    The Interquartile Range (IQR) method is applied to remove outliers, but importantly, this is done **per `location` group**. This handles the fact that what might be an outlier in one location (e.g., a very large property in a city center) might be normal in another (e.g., a farmhouse in an outskirts area).

    1.  **Clipping `total_sqft` Outliers:**
        For each `location` group, the Q1, Q3, and IQR of `total_sqft` are calculated. Upper and lower limits (Q3 + 1.5\*IQR, Q1 - 1.5\*IQR) are determined. Any `total_sqft` value outside these limits *for that specific location* is clipped (replaced by the respective limit). The processed groups are concatenated into `df6`.
        ```python
        df6 = pd.DataFrame()
        for location,group in df5.groupby('location'):
          q1 = group['total_sqft'].quantile(0.25)
          q3 = group['total_sqft'].quantile(0.75)
          iqr = q3 - q1
          upper_limit = q3 + 1.5 * iqr
          lower_limit = q1 - 1.5 * iqr
          group['total_sqft'] = group['total_sqft'].clip(upper = upper_limit, lower = lower_limit)
          df6 = pd.concat((df6 , group))
        ```
        Box plots of `total_sqft` per location are re-generated to show the effect of clipping.

    2.  **Clipping `PPS` Outliers and Recalculating `price`:**
        The same IQR-based clipping process is applied to `PPS` values, again **per `location` group**. After clipping `PPS` values, the `price` column is **recalculated** using the adjusted `total_sqft` and `PPS` values to ensure consistency. The processed groups are concatenated into `df7`.
        ```python
        df7 = pd.DataFrame()
        for location,group in df6.groupby('location'):
          q1 = group['PPS'].quantile(0.25)
          q3 = group['PPS'].quantile(0.75)
          iqr = q3 - q1
          upper_limit = q3 + 1.5 * iqr
          lower_limit = q1 - 1.5 * iqr
          group['PPS'] = group['PPS'].clip(upper = upper_limit, lower = lower_limit)
          df7 = pd.concat((df7 , group))
        df7['price'] = (df7['total_sqft'] * df7['PPS'])/100000 # Recalculate price
        ```
        Box plots of `PPS` and `price` per location are re-generated to visualize the effect of clipping.
        `df6.describe()` and `df7.describe()` are used to compare the statistics before and after outlier treatment.

## 4. Feature Engineering and Encoding for Machine Learning

Features need to be transformed into a numerical format suitable for machine learning models.

* **Categorical to Numerical Mapping:**
    * `area_type`: Mapped to `0` for 'super built-up area' and `1` for 'Others'.
    * `availability`: Mapped to `0` for 'Ready To Move' and `1` for 'UC'.
    ```python
    df7['area_type'] = df7['area_type'].map({'super built-up area':0,  'Others':1})
    df7['availability'] = df7['availability'].map({'Ready To Move':0,  'UC':1})
    df7.head()
    ```
* **One-Hot Encoding for `location`:**
    Since `location` is a categorical column with multiple unique values, `pd.get_dummies()` is used to convert it into a numerical (binary) representation. Each unique location becomes a new column with 0s and 1s. `dtype=int` ensures the output dummy variables are integers.
    ```python
    df8 = pd.get_dummies(df7,dtype=int)
    df8.head()
    ```
* **Log Transformation for Target (`price`):**
    * The distribution of `price` is often skewed, which can negatively impact linear regression models. A histogram of `y` (price) and `np.log(y)` (log-transformed price) is plotted to visualize the effect of transformation.
    * The target variable `y` is log-transformed (`Yt = np.log(y)`) to normalize its distribution, make it more Gaussian, and stabilize variance, leading to potentially better model performance.
    ```python
    y.plot.hist() # Histogram of original price
    np.log(y).plot.hist() # Histogram of log-transformed price
    Yt = np.log(y)
    ```

## 5. Model Training and Evaluation (Multiple Linear Regression)

A `LinearRegression` model is built to predict the log-transformed `price` based on the processed features.

* **Feature and Target Selection:**
    * `X`: Includes all processed features from `df8` except 'price' and 'PPS' (as PPS was an intermediate calculation and price is the target).
    * `Yt`: The log-transformed 'price'.
    ```python
    X = df8.drop(columns=['price', 'PPS'])
    y = df8['price'] # Note: `y` here is the original price, `Yt` is the log-transformed target used for training
    ```
* **Data Scaling (MinMaxScaler for Features):**
    Features in `X` are scaled to a range of [0, 1] using `MinMaxScaler` to ensure that features with larger numerical values do not dominate the learning process.
    ```python
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    scaler.fit(X)
    Xscaled = scaler.transform(X) # Xscaled is the scaled feature matrix
    ```
* **Data Splitting:** The scaled features (`Xscaled`) and log-transformed target (`Yt`) are split into training and testing sets.
    ```python
    from sklearn.model_selection import train_test_split
    xtrain, xtest, ytrain, ytest = train_test_split(Xscaled,Yt)
    ```
* **Model Training:** A `LinearRegression` model (`modelA`) is initialized and trained on the `xtrain` and `ytrain` data.
    ```python
    from sklearn.linear_model import LinearRegression
    modelA = LinearRegression()
    modelA.fit(xtrain,ytrain)
    ```
* **Model Evaluation:**
    * **Predictions:** `ytrainPred` and `ytestPred` are the predictions on the training and test sets, respectively.
    * **Mean Absolute Error (MAE):** Calculated for both training and test sets to quantify the average prediction error.
        ```python
        ytrainPred = modelA.predict(xtrain)
        ytestPred = modelA.predict(xtest)
        print("Mean absolute error(Train)-" , abs(ytrain - ytrainPred).mean())
        print("Mean absolute error(Test)-" , abs(ytest - ytestPred).mean())
        ```
    * **R-squared Score (`r2_score`):** Measures the proportion of variance in the dependent variable that can be predicted from the independent variables. A higher R-squared indicates a better fit.
        ```python
        from sklearn.metrics import r2_score
        print("r2_score_train" , r2_score(ytrain,ytrainPred))
        print("r2_score_test" , r2_score(ytest,ytestPred))
        ```
* **Feature Coefficients:** The coefficients of the `LinearRegression` model indicate the importance and direction of influence of each feature on the target variable. These are displayed as a bar plot.
    ```python
    feature_coef = pd.DataFrame(modelA.coef_)
    feature_coef.index = X.columns
    feature_coef.plot.bar(figsize = (30,5))
    ```

## 6. Model Deployment Preparation (Artifacts)

To deploy the trained model for future predictions, its essential components are saved as "artifacts".

* **Save Model:** The trained `modelA` is saved using `joblib.dump` as `real_estate.pkl`.
    ```python
    import joblib
    joblib.dump(modelA , "real_estate.pkl")
    ```
* **Save Scaler:** The `MinMaxScaler` object, crucial for scaling new input data consistently with training data, is saved as `feature_scaling.pkl`.
    ```python
    joblib.dump(scaler, 'feature_scaling.pkl')
    ```
* **Save Training Data Columns:** The list of column names (features) used during training is saved as a JSON file (`training_data_columns.json`). This ensures that new input data for prediction has the features in the correct order and format.
    ```python
    import json
    training_data_columns = {"data_columns" : X.columns.to_list()}
    json_data = json.dumps(training_data_columns)
    my_json_file = open("training_data_columns.json" , "w")
    my_json_file.write(json_data)
    my_json_file.close()
    ```

## 7. Prediction on New Input Data

This section demonstrates how to use the saved artifacts to make predictions on new, unseen property data.

* **Sample Input Data:** Example values for a new property are defined.
    ```python
    area_type = "Super built-up Area"
    availability = "Ready To Move"
    location = "5th phase jp nagar"
    size = 2
    total_sqft = 1200
    bath = 2
    balcony = 2
    ```
* **Prepare Input Array:** A NumPy array of zeros is initialized with the same length as the training data columns. The sample input values are then placed into this array at their correct positions.
    * Categorical `area_type` and `availability` are mapped to their numerical equivalents (0 or 1) using predefined lambda functions.
    * Numerical features (`size`, `total_sqft`, `bath`, `balcony`) are assigned directly.
    * For the one-hot encoded `location`, the index of the specific location column is found using `X.columns.to_list().index("location_" + location)` and set to 1.
    ```python
    input = np.zeros(len(X.columns))
    area_type_function = lambda area_type : 0 if area_type.lower().strip() == 'super built-up area' else 1
    availability_function = lambda availability : 0 if availability == 'Ready To Move' else 1

    input[0] = area_type_function(area_type)
    input[1] = availability_function(availability)
    input[2] = size
    input[3] = total_sqft
    input[4] = bath
    input[5] = balcony
    # For location, set the corresponding one-hot encoded index to 1
    # Assuming 'location_5th phase jp nagar' is at index 6 in X.columns
    input[6] = 1 # This index needs to be dynamically determined in a real application
    print(input)
    ```
* **Load Saved Artifacts:** The trained model and scaler objects are loaded back into memory.
    ```python
    _model = joblib.load('/content/real_estate.pkl')
    _scaling = joblib.load('/content/feature_scaling.pkl')
    ```
* **Make Prediction:** The prepared `input` array is scaled using the loaded `_scaling` object and then passed to the `_model.predict()` method.
    ```python
    predicted_log_price = _model.predict(_scaling.transform([input]))
    print(predicted_log_price) # This is the log-transformed predicted price
    ```
* **Convert Log Price to Original Scale:** Since the model was trained on log-transformed prices, the prediction is exponentiated (`np.exp()`) to get the price back in its original scale (e.g., in lakhs).
    ```python
    print(np.exp(predicted_log_price)) # This is the final predicted price in original scale
    ```
