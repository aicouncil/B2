# Topics Covered in `el_ds_7(ml_classification).ipynb`

This notebook demonstrates the process of solving a machine learning classification problem using the Iris dataset. The main focus is on building, evaluating, visualizing, and tuning a Decision Tree Classifier. Below are the key topics covered, with explanations and examples.

---

## 1. Loading and Exploring the Iris Dataset

**Explanation:**  
The dataset is loaded using pandas from a CSV file. The first few rows are displayed to get a sense of the data.

**Example:**
```python
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/Iris.csv')
df.head()
```

---

## 2. Data Inspection

**Explanation:**  
The code checks the unique species in the dataset, which is essential for understanding the target classes.

**Example:**
```python
df['Species'].unique()
# Output: array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], dtype=object)
```

---

## 3. Classification Problem Definition

**Explanation:**  
The problem is framed as predicting the species of an iris flower given its physical measurements.

**Example (Markdown in the notebook):**
> **Build a predictive model to predict flower species if we know "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm".**

---

## 4. Data Preprocessing

**Explanation:**  
Splitting the data into features (`X`) and target (`y`). The dataset is then split into training and testing sets.

**Example:**
```python
X = df.drop(columns=['Id', 'Species'])
y = df['Species']

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, train_size=0.75)
```

---

## 5. Training a Decision Tree Classifier

**Explanation:**  
A Decision Tree model is trained on the training data.

**Example:**
```python
from sklearn.tree import DecisionTreeClassifier

modelA = DecisionTreeClassifier()
modelA.fit(xtrain, ytrain)
```

---

## 6. Evaluating the Classifier

**Explanation:**  
The accuracy of the classifier is measured on both the training and testing data to assess performance.

**Example:**
```python
print(modelA.score(xtrain, ytrain))  # Training accuracy
print(modelA.score(xtest, ytest))    # Testing accuracy
```

---

## 7. Overfitting Discussion

**Explanation:**  
The notebook notes that using a Decision Tree without tuning can lead to overfitting (very high training accuracy but lower test accuracy).

**Example (Markdown in the notebook):**
> **Decision tree classifier without tuning or using limiting criteria - it will lead you to overfit model**

---

## 8. Visualizing the Decision Tree

**Explanation:**  
The structure of the Decision Tree is visualized to better understand the decision process.

**Example:**
```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12,10))
plot_tree(modelA, feature_names=xtrain.columns)
plt.show()
```

---

## 9. Hyperparameter Tuning with Grid Search CV

**Explanation:**  
Grid Search with cross-validation (`GridSearchCV`) is used to find the best hyperparameters for the Decision Tree, helping to avoid overfitting and improving performance.

**Example:**
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'min_samples_leaf': [5, 7, 9, 11, 13, 15],
    'max_leaf_nodes': [4, 5, 6, 7, 8],
    'max_depth': [2, 3, 4, 5]
}

modelB = DecisionTreeClassifier()
gridModel = GridSearchCV(modelB, param_grid)
gridModel.fit(xtrain, ytrain)
```

---

## Summary

This notebook guides you through:
- Loading and inspecting data,
- Framing a classification problem,
- Training and evaluating a machine learning model,
- Visualizing the model,
- Tuning model hyperparameters for better generalization.

These steps are foundational for any supervised classification task in machine learning.
