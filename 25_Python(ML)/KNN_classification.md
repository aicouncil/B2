# KNN (K-Nearest Neighbors) Classification – Detailed Explanation & Examples

This notebook demonstrates the basics of the K-Nearest Neighbors (KNN) algorithm for classification using the Iris dataset. Below, each concept is explained in detail, including examples and code snippets.

---

## 1. Introduction to KNN

**K-Nearest Neighbors (KNN)** is a simple, intuitive supervised machine learning algorithm used for classification and regression.  
- For classification, it assigns the class most common among its K nearest neighbors.
- For regression, it averages the values of its K nearest neighbors.

**How it works:**
- Given a new data point, the algorithm calculates the distance (often Euclidean) from this point to all points in the training set.
- It selects the K closest points (neighbors).
- For classification, the new point is assigned to the most frequent class among these neighbors.

**Example:**  
If K=3 and among the three nearest neighbors, two belong to class "A" and one to class "B", the new point is classified as "A".

---

## 2. Loading the Dataset

In this notebook, the **Iris dataset** is used. It is a classic dataset in machine learning, containing measurements for three types of iris flowers.

```python
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/Iris.csv')
df.head()
```

**Output:**

| Id | SepalLengthCm | SepalWidthCm | PetalLengthCm | PetalWidthCm | Species       |
|----|---------------|--------------|---------------|--------------|--------------|
| 1  | 5.1           | 3.5          | 1.4           | 0.2          | Iris-setosa  |
| 2  | 4.9           | 3.0          | 1.4           | 0.2          | Iris-setosa  |
| ...| ...           | ...          | ...           | ...          | ...          |

---

## 3. Data Exploration

### 3.1 Checking Dataset Shape

```python
df.shape
```
**Output:**  
`(150, 6)`  
_This means the dataset has 150 rows and 6 columns._

### 3.2 Checking Unique Classes

```python
df['Species'].unique()
```
**Output:**  
`array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], dtype=object)`

_There are three classes of iris species._

---

## 4. Manual KNN Implementation

### 4.1 Creating a Copy of the DataFrame

To avoid modifying the original data:
```python
df1 = df.copy()
```

### 4.2 Defining a New Sample

Suppose you have a new flower with the following features:

```python
new_feature = [3.1, 2.5, 3.4, 3.9]  # [SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]
```

---

## 5. Calculating Distance from the New Sample

The Euclidean distance formula for two points A and B in n-dimensional space is:
\[
d = \sqrt{(a_1-b_1)^2 + (a_2-b_2)^2 + ... + (a_n-b_n)^2}
\]

**In code:**
```python
df1['distances'] = ((df['SepalLengthCm'] - new_feature[0])**2 + 
                    (df['SepalWidthCm'] - new_feature[1])**2 + 
                    (df['PetalLengthCm'] - new_feature[2])**2 + 
                    (df['PetalWidthCm'] - new_feature[3])**2)
```

Now, every row in `df1` has a new column `'distances'` representing its distance from the new sample.

---

## 6. Sorting by Distance (Finding Nearest Neighbors)

Sort the DataFrame by the `'distances'` column to find the nearest neighbors:
```python
df1_sorted = df1.sort_values(by='distances')
df1_sorted.head(5)
```

**Output Example:**

| Id | SepalLengthCm | ... | Species           | distances |
|----|---------------|-----|-------------------|-----------|
| 58 | 4.9           | ... | Iris-versicolor   | 0.1296    |
| 94 | 5.0           | ... | Iris-versicolor   | 0.5776    |
| 61 | 5.0           | ... | Iris-versicolor   | 0.9409    |
| ...| ...           | ... | ...               | ...       |

_These are the five closest points to your new sample. Their `Species` could be used for majority voting to classify the new point._

---

## 7. Predicting the Class

Suppose K=3.  
- Look at the top 3 rows in `df1_sorted`.
- Find out which `Species` is most common among these rows.
- Assign that as the predicted class for your new sample.

**Example:**
If the top three neighbors are all "Iris-versicolor", the new flower will be classified as "Iris-versicolor".

---

## 8. Summary of Steps

1. Load and explore the dataset.
2. Define the new sample.
3. Calculate distances from the new sample to all data points.
4. Sort by distance to get the nearest neighbors.
5. Use majority vote among neighbors to predict the class.

---

## 9. Complete Example Code

```python
import pandas as pd

# 1. Load data
df = pd.read_csv('https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/Iris.csv')

# 2. Define new sample
new_feature = [3.1, 2.5, 3.4, 3.9]

# 3. Calculate distances
df1 = df.copy()
df1['distances'] = ((df['SepalLengthCm'] - new_feature[0])**2 + 
                    (df['SepalWidthCm'] - new_feature[1])**2 + 
                    (df['PetalLengthCm'] - new_feature[2])**2 + 
                    (df['PetalWidthCm'] - new_feature[3])**2)

# 4. Sort and get K nearest neighbors
K = 3
df1_sorted = df1.sort_values(by='distances')
top_k = df1_sorted.head(K)

# 5. Predict class
predicted_class = top_k['Species'].mode()[0]
print(f"The predicted class for the new sample is: {predicted_class}")
```

---

## 10. Notes

- The value of K is a parameter you can choose; it should be odd to reduce ties in classification.
- Feature scaling is important in KNN, as different ranges can bias the distance calculation.
- Libraries like `scikit-learn` provide optimized implementations of KNN for both classification and regression.

---

# References

- [Iris Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)
- [K-Nearest Neighbors Algorithm - Wikipedia](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
- [scikit-learn KNN Documentation](https://scikit-learn.org/stable/modules/neighbors.html)
