# Support Vector Machine (SVM) – A Step-by-Step Guide

This document provides a detailed explanation of the concepts, workflow, and Python code involved in the file `b12_support_vector_machine_1.ipynb`, which demonstrates the use of Support Vector Machine (SVM) for classification problems. The example uses a diabetes dataset for predicting diabetes risk.

---

## Table of Contents

1. [Introduction to Support Vector Machines (SVM)](#introduction)
2. [Data Loading and Exploration](#data-loading)
3. [Data Preparation](#data-preparation)
4. [Training a Support Vector Classifier](#training-svc)
5. [Model Evaluation](#model-evaluation)
6. [Kernel Functions in SVM](#kernel-functions)
7. [Hyperparameter Tuning](#hyperparameter-tuning)
8. [Summary](#summary)

---

<a name="introduction"></a>
## 1. Introduction to Support Vector Machines (SVM)

SVM is a powerful supervised machine learning algorithm used for classification and regression tasks. Its main goal is to find the optimal hyperplane that best separates data points of different classes in the feature space.

### Key Concepts

- **Hyperplane**: A decision boundary that separates different classes.
- **Support Vectors**: The data points closest to the hyperplane; they are critical in defining the position and orientation of the hyperplane.
- **Margin**: The distance between the hyperplane and the nearest support vectors. SVM aims to maximize this margin.

#### Visual Example

Suppose we have two classes (Red and Blue). SVM finds the line (in 2D) or hyperplane (in higher dimensions) that maximally separates these points.

```
Red points (class 0): o o o
Blue points (class 1): x x x

SVM will find a line that best separates o and x, with the widest possible gap between the nearest o and x.
```

---

<a name="data-loading"></a>
## 2. Data Loading and Exploration

The dataset used is a diabetes health record containing features like Age, BMI, Blood Pressure, etc., and the target variable is `DiabetesRisk`.

```python
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/diabetes_data.csv')
df.head()
```

**Sample Columns:**
- Age
- BMI
- BloodPressure
- GlucoseLevel
- InsulinLevel
- PhysicalActivityLevel
- FamilyHistory
- Smoking
- DiabetesRisk (target)

**Example Output:**

| Age | BMI  | BloodPressure | GlucoseLevel | InsulinLevel | ... | DiabetesRisk |
|-----|------|---------------|--------------|--------------|-----|--------------|
| 58  | 27.0 | 73.2          | 84.9         | 91.2         | ... | 0            |
| 71  | 24.9 | 87.1          | 95.8         | 72.2         | ... | 0            |

---

<a name="data-preparation"></a>
## 3. Data Preparation

### Splitting Features and Target

```python
X = df.drop(columns = 'DiabetesRisk')
y = df['DiabetesRisk']
```

### Train-Test Split

Splitting the dataset into training (75%) and testing (25%) portions.

```python
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, train_size=0.75)
```

### Feature Scaling

SVM is sensitive to the scale of the data. We use MinMaxScaler to scale all features to the range [0, 1].

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(xtrain)
xtrainScaled = scaler.transform(xtrain)
xtestScaled = scaler.transform(xtest)
```

---

<a name="training-svc"></a>
## 4. Training a Support Vector Classifier

We use scikit-learn's `SVC` (Support Vector Classifier) to train our model.

```python
from sklearn.svm import SVC
model_svc = SVC(degree=2)
model_svc.fit(xtrainScaled, ytrain)
```

**Explanation:**
- `degree=2` specifies the degree for the polynomial kernel (default kernel is 'rbf', but degree is relevant for 'poly').
- The model is trained on the scaled training data.

---

<a name="model-evaluation"></a>
## 5. Model Evaluation

### Accuracy Scores

We evaluate our model on both training and test sets.

```python
print(model_svc.score(xtrainScaled, ytrain))  # Training accuracy
print(model_svc.score(xtestScaled, ytest))    # Testing accuracy
```

**Example Output:**
```
0.897  # (Training accuracy)
0.848  # (Testing accuracy)
```

### Confusion Matrix

A confusion matrix shows the number of correct and incorrect predictions made by the classifier.

```python
from sklearn.metrics import confusion_matrix
print(confusion_matrix(ytest, model_svc.predict(xtestScaled)))
```

**Example Output:**
```
[[132  13]
 [ 25  80]]
```
- The diagonal values (132 and 80) are correct predictions.
- The off-diagonal values (13 and 25) are misclassifications.

---

<a name="kernel-functions"></a>
## 6. Kernel Functions in SVM

SVM can use different kernel functions to transform data into a higher-dimensional space for better separation.

### Common Kernels:
- **Linear**: For linearly separable data.
- **Polynomial (poly)**: For data that is not linearly separable.
- **Radial Basis Function (rbf)**: For complex, non-linear boundaries.

#### Example: Using Polynomial Kernel

```python
model_svc_poly = SVC(kernel='poly', degree=6)
model_svc_poly.fit(xtrainScaled, ytrain)
print(model_svc_poly.score(xtrainScaled, ytrain))  # Training accuracy
print(model_svc_poly.score(xtestScaled, ytest))    # Test accuracy
```

**Output:**
```
0.984  # Training accuracy
0.876  # Test accuracy
```

---

<a name="hyperparameter-tuning"></a>
## 7. Hyperparameter Tuning

To find the best degree for the polynomial kernel, we loop over several values and record the results.

```python
train_accuracy = []
test_accuracy = []
for i in range(1, 12):
    model_svc_poly = SVC(kernel='poly', degree=i)
    model_svc_poly.fit(xtrainScaled, ytrain)
    train_score = model_svc_poly.score(xtrainScaled, ytrain)
    test_score = model_svc_poly.score(xtestScaled, ytest)
    train_accuracy.append(train_score)
    test_accuracy.append(test_score)
```

You can then visualize these results with a plot:

```python
import matplotlib.pyplot as plt

plt.plot(range(1, 12), train_accuracy, label='Train Accuracy')
plt.plot(range(1, 12), test_accuracy, label='Test Accuracy')
plt.xlabel('Polynomial Degree')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
```

**Interpretation:**  
- This helps identify the degree with the best trade-off between training and test accuracy, avoiding overfitting.

---

<a name="summary"></a>
## 8. Summary

- SVM is a robust classifier, especially effective for high-dimensional data.
- Proper data preprocessing and scaling are essential for SVM performance.
- Kernel choice and hyperparameter tuning (like polynomial degree) significantly affect results.
- Model evaluation should always consider both accuracy scores and confusion matrices for a full picture.

---

### References

- [scikit-learn SVM Documentation](https://scikit-learn.org/stable/modules/svm.html)
- [Original Diabetes Dataset](https://github.com/bipulshahi/Dataset)

---
