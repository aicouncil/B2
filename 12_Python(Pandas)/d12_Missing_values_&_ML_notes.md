## Handling Missing Values

When working with real-world data, it's common to encounter missing values. Handling these values properly is crucial for accurate analysis and modeling.

### Detecting Missing Values

You can detect missing values in your DataFrame using:
```python
df.isnull().sum()
```
This will show the count of missing (`NaN`) values in each column.

### Filling Missing Values

- **For numerical columns:** Fill missing values with the mean or median.
    ```python
    df['Item_Weight'].fillna(df['Item_Weight'].mean(), inplace=True)
    ```
- **For categorical columns:** Fill missing values with the mode (most frequent value).
    ```python
    df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0], inplace=True)
    ```

### Verifying

After filling, check again for missing values:
```python
df.isnull().sum()
```

---

## What is Machine Learning?

Machine Learning (ML) is a subset of Artificial Intelligence (AI) that involves the development of algorithms that allow computers to learn patterns from data and make predictions or decisions without being explicitly programmed for each task.

**Key Points:**
- ML algorithms improve their performance automatically through experience.
- ML is widely used for data-driven predictions, decision-making, and automation.

### Main Types of Machine Learning

1. **Supervised Learning**
2. **Unsupervised Learning**
3. **Reinforcement Learning**

---

## Supervised Learning

Supervised learning is a type of machine learning where the algorithm is trained on labeled data. That is, the input data comes with the correct output, and the algorithm learns to map inputs to outputs.

### Types of Supervised Learning:

- **Regression**
- **Classification**

---

### Regression

**Definition:**  
Regression is used when the target variable is continuous and numerical. The goal of regression is to predict a quantity.

**Example:**  
Predicting house prices based on features like area, number of bedrooms, location, etc.

```python
# Example: Predicting house price
# Features: Area (sq ft), Number of bedrooms
# Target: Price (in dollars)

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'Area': [1000, 1500, 2000, 2500],
        'Bedrooms': [2, 3, 3, 4],
        'Price': [200000, 280000, 340000, 400000]}
df = pd.DataFrame(data)

X = df[['Area', 'Bedrooms']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)
print(model.predict([[1800, 3]]))  # Predict price for 1800 sq ft, 3 bedrooms
```

**Common Regression Algorithms:**
- Linear Regression
- Ridge/Lasso Regression
- Decision Tree Regression
- Random Forest Regression

---

### Classification

**Definition:**  
Classification is used when the target variable is categorical. The goal is to assign each input to one of a fixed number of categories.

**Example:**  
Predicting whether an email is "spam" or "not spam" (binary classification), or classifying handwritten digits (0–9) in the MNIST dataset (multi-class classification).

```python
# Example: Classifying emails as spam or not spam
# Features: Email text, presence of specific words, etc.
# Target: Spam (1) or Not Spam (0)

import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {'Word_Count': [120, 300, 150, 80],
        'Contains_Link': [1, 0, 1, 0],
        'Spam': [0, 1, 0, 0]}
df = pd.DataFrame(data)

X = df[['Word_Count', 'Contains_Link']]
y = df['Spam']

model = LogisticRegression()
model.fit(X, y)
print(model.predict([[200, 1]]))  # Predict for 200 words, contains link
```

**Common Classification Algorithms:**
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

---

### Regression vs Classification

| Aspect               | Regression                          | Classification                       |
|----------------------|-------------------------------------|--------------------------------------|
| Output type          | Continuous numerical value          | Discrete class label                 |
| Example target       | House price, temperature            | Spam/Not Spam, Disease/No Disease    |
| Evaluation metrics   | Mean Squared Error, R² Score        | Accuracy, Precision, Recall, F1 Score|
| Example algorithms   | Linear Regression, Random Forest    | Logistic Regression, Random Forest   |

---

### Summary Table

| Learning Type | Target Variable | Example           | Typical Algorithms         |
|---------------|-----------------|-------------------|---------------------------|
| Regression    | Continuous      | House Prices      | Linear Regression         |
| Classification| Categorical     | Email Spam/Not    | Logistic Regression, SVM  |

---

## Conclusion

- **Handling missing values** is an essential preprocessing step in any data science workflow.
- **Machine Learning** enables computers to learn from data and make predictions.
- **Supervised Learning** is the most common paradigm, with **regression** for continuous targets and **classification** for categorical targets.
- Choosing the right approach and algorithm depends on the nature of your target variable and the problem you are solving.
