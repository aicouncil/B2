# Handling Biased Models: Evaluation and Remedies

In the notebook "el_ds_6(ml_classification).ipynb", the following concepts and techniques are explained in this order, with examples:

---

## 1. Confusion Matrix

**Definition:**  
A confusion matrix is a table layout that allows visualization of the performance of a classification algorithm.

**Purpose:**  
It shows the counts of true positives, true negatives, false positives, and false negatives.

**Importance:**  
Helps to understand which classes are being misclassified and the types of errors made by the model.

**Example (sklearn):**
```python
from sklearn.metrics import confusion_matrix
y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 0, 1, 1]
cm = confusion_matrix(y_true, y_pred)
print(cm)
# Output:
# [[1 1]
#  [1 2]]
```

---

## 2. Classification Report

**Definition:**  
The classification report provides key metrics: precision, recall, f1-score, and support for each class.

**Purpose:**  
Offers a detailed evaluation of model performance for each class, which is especially important for imbalanced datasets.

**Metrics Explained:**
- **Precision:** How many selected items are relevant?
- **Recall:** How many relevant items are selected?
- **F1-score:** Harmonic mean of precision and recall.
- **Support:** Number of actual occurrences of the class.

**Example (sklearn):**
```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
# Output:
#               precision    recall  f1-score   support
#            0       0.50      0.50      0.50         2
#            1       0.67      0.67      0.67         3
```

---

## 3. Oversampling / Undersampling

**Oversampling:**  
Increases the number of samples in the minority class (e.g., using SMOTE) to balance the dataset.

**Undersampling:**  
Reduces the number of samples from the majority class to match the minority class.

**Purpose:**  
Both methods aim to address class imbalance, making the classifier less biased towards the majority class.

**Example (SMOTE - oversampling):**
```python
from imblearn.over_sampling import SMOTE
smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X, y)
```

**Example (Random Undersampling):**
```python
from imblearn.under_sampling import RandomUnderSampler
rus = RandomUnderSampler()
X_res, y_res = rus.fit_resample(X, y)
```

---

## 4. Class Weight Adjustment

**Definition:**  
Many machine learning classifiers offer a `class_weight` parameter that can be set to `'balanced'`.

**How it works:**  
Adjusts the weights inversely proportional to class frequencies, so the model gives more attention to the minority class during training.

**When to use:**  
Especially useful when you want to train on the original data but still counteract class imbalance.

**Example (Logistic Regression):**
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(class_weight='balanced')
model.fit(X_train, y_train)
```

---

## Summary Table

| Concept                | Purpose                                                         | Example Code/Function         |
|------------------------|-----------------------------------------------------------------|------------------------------|
| Confusion Matrix       | Visualizes prediction outcomes and types of classification errors| sklearn.metrics.confusion_matrix |
| Classification Report  | Provides precision, recall, f1-score, and support per class     | sklearn.metrics.classification_report |
| Oversampling/Undersampling | Balances class distribution in the training data             | imblearn.over_sampling.SMOTE, imblearn.under_sampling.RandomUnderSampler |
| Class Weight Adjustment| Compensates for class imbalance during model training           | class_weight='balanced' in classifiers |

---

These steps help ensure a more balanced and fair classification model, particularly when working with imbalanced datasets.
