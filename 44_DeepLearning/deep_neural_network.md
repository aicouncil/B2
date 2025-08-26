### Machine Learning Model Building and Evaluation

This document provides a detailed explanation of the machine learning model building process for a customer churn prediction task, as demonstrated in the provided Python file. The focus is on building a baseline model, addressing the common problem of imbalanced data, and implementing Logistic Regression.

-----

#### 1\. Data Preparation for Modeling

Before building a model, the preprocessed data is prepared for training. The `df2` DataFrame, which has had its irrelevant columns dropped and its categorical columns encoded, is used as the starting point.

  * **Feature and Target Selection:** The preprocessed data is split into **features (`X`)** and the **target variable (`y`)**. The features include all columns except `Exited`, and the target is the `Exited` column itself.
    ```python
    X = df2.drop(columns = ['Exited'])
    y = df2['Exited']
    ```
  * **Data Scaling:** Data scaling is a crucial preprocessing step for many machine learning algorithms, especially those that rely on distance metrics, like K-Nearest Neighbors (KNN). The `MinMaxScaler` is used to scale all numerical features to a range of 0 to 1, ensuring that no single feature dominates the model's learning process due to its large magnitude.
    ```python
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    scaler.fit(X)
    Xscaled = scaler.transform(X)
    ```
  * **Data Splitting:** The scaled data is partitioned into training (`xtrain`, `ytrain`) and test (`xtest`, `ytest`) sets using `train_test_split`. The training set is used to train the model, while the test set is reserved for evaluating its performance on unseen data.
    ```python
    from sklearn.model_selection import train_test_split
    xtrain, xtest, ytrain, ytest = train_test_split(Xscaled,y)
    ```

-----

#### 2\. Baseline Model and Evaluation (K-Nearest Neighbors)

A baseline model is built and evaluated to provide a benchmark for future model performance.

  * **Model Training:** A `KNeighborsClassifier` model (`modelA`) is trained by fitting it to the training data (`xtrain`, `ytrain`).
    ```python
    from sklearn.neighbors import KNeighborsClassifier
    modelA = KNeighborsClassifier()
    modelA.fit(xtrain,ytrain)
    ```
  * **Evaluation:** The model's accuracy is evaluated using the `.score()` method on both the training and test data.
    ```python
    print("Model accuracy on training data -",modelA.score(xtrain,ytrain))
    print("Model accuracy on test data -",modelA.score(xtest,ytest))
    ```

-----

#### 3\. Handling and Working with Biased Data

The dataset has a significant imbalance, with a large number of customers who did not churn and a small number who did. The notebook shows this imbalance with `y.value_counts()`. This can lead to a **biased model** that simply predicts the majority class, making simple accuracy a misleading metric.

  * **Evaluation with Advanced Metrics:** The `confusion_matrix` and `classification_report` are used to provide a more detailed evaluation of the model's performance on each class. The classification report provides **precision, recall, and F1-score**, which are better indicators of a model's bias and true effectiveness.
  * **Technique 1: Undersampling:**
      * **Definition:** Undersampling is a technique that balances the dataset by randomly removing samples from the majority class.
      * **Implementation:** The `RandomUnderSampler` from the `imblearn` library is used to create a new, balanced dataset (`Xu`, `yu`). A new KNN model (`modelB`) is then trained on this data and evaluated with the `classification_report`.
  * **Technique 2: Oversampling:**
      * **Definition:** Oversampling balances the dataset by increasing the number of samples in the minority class. The **SMOTE** (Synthetic Minority Over-sampling Technique) algorithm is used to generate synthetic data points for the minority class.
      * **Implementation:** The `SMOTE` class from `imblearn.over_sampling` is used to create a balanced dataset (`Xo`, `yo`). A new KNN model (`modelC`) is trained and evaluated on this data, showing a more balanced `classification_report`.
  * **Technique 3: Class Weight Management:** This technique is a model-level approach that assigns a higher penalty to misclassifications of the minority class, forcing the model to pay more attention to it without changing the data distribution.

-----

#### 4\. Logistic Regression Model

**Definition:** Logistic Regression is a statistical model used for **binary classification**. It predicts the probability of an instance belonging to a certain class by passing a linear combination of features through a **sigmoid function** to map the output to a value between 0 and 1.

  * **Mechanism (Sigmoid Function):** The sigmoid function, $f(z) = \\frac{1}{1 + e^{-z}}$, is a key component. The script provides examples to show how the output of this function changes with different inputs, demonstrating how it converts a linear output into a probability.
    ```python
    x = 1; w0 = 1e-2; w1 = 1e-2
    z = 1/(1 + np.exp(-(w0 + w1*x)))
    print(z) # Output: ~0.505
    ```
    With larger values of `x` and `w`, the output of `z` approaches 1.
  * **Training on Imbalanced Data:** A `LogisticRegression` model (`model_log_A`) is trained on the original, imbalanced data. Its `classification_report` shows the expected bias towards the majority class.
  * **Training with Class Weights:** A `LogisticRegression` model (`model_log_D`) is trained on the original data but with a `class_weight` parameter set to `{0:1 , 1:6}`. This assigns a weight of 6 to the minority class (`1`), forcing the model to pay more attention to it during training.
    ```python
    from sklearn.linear_model import LogisticRegression
    model_log_D = LogisticRegression(class_weight={0:1 , 1:6})
    model_log_D.fit(xtrain,ytrain)
    ```
    This approach, as shown by the `classification_report`, effectively improves the model's ability to identify the minority class. The `model_log_D.coef_` attribute provides the learned coefficients (weights) for each feature, which can be used to interpret the model's decision-making process.
