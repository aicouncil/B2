# Unsupervised Learning: Clustering & K-Means Algorithm

## 1. Introduction to Unsupervised Learning

Unsupervised learning is a type of machine learning where the model works with data that does **not have predefined labels**. The main goal is to uncover hidden structures or patterns within the data.

### Key Points:
- **No Labels:** Data is unlabelled.
- **Objective:** Discover patterns, groupings, or associations.
- **Popular Methods:** Clustering, Dimensionality Reduction.

---

## 2. Clustering

Clustering is the process of grouping data points such that points in the same group (cluster) are more similar to each other than to those in other groups.

### Main Steps in Clustering:
1. **Label the Unlabelled Data:** Assign cluster labels to previously unlabelled data.
2. **Find Similar Data Events:** Group data points with similar properties.
3. **Form Clusters:** Create groups based on similarity.
4. **Assign Labels:** Each cluster is given a unique label or identifier.
5. **Statistical Analysis:** Analyze clusters to understand their significance.

### Example Dataset

Suppose we have a simple dataset with two features (`x`, `y`):

```python
import pandas as pd

data = pd.DataFrame({
    'x': [12,24,28,33,18,29,52,45,24,55,51,61,53,69,72,64,49,58],
    'y': [36,39,30,52,54,46,55,59,63,70,66,63,58,23,14,8,19,7]
})
print(data)
```

---

## 3. Data Visualization

Visualizing data points helps in understanding the distribution and possible clusters.

```python
import matplotlib.pyplot as plt

plt.scatter(data['x'], data['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot of data points')
plt.show()
```

---

## 4. Choosing Number of Clusters

Often, the number of clusters is not known beforehand. Visual inspection can help hypothesize the number (e.g., 3 clusters in this sample).

---

## 5. K-Means Algorithm

K-Means is a popular clustering algorithm that partitions data into `K` clusters by minimizing the variance within each cluster.

### Steps in K-Means:

#### Step 1: Initialize Centroids
Randomly select `K` initial centroids.

```python
import numpy as np

cent1 = [np.random.randint(10,70), np.random.randint(10,70)]
cent2 = [np.random.randint(10,70), np.random.randint(10,70)]
cent3 = [np.random.randint(10,70), np.random.randint(10,70)]

print("Initial centroids:", cent1, cent2, cent3)
```

#### Step 2: Assign Points to Nearest Centroid

Calculate Euclidean distance from each point to each centroid and assign to the nearest one.

```python
data['r'] = ((data['x'] - cent1[0])**2 + (data['y'] - cent1[1])**2)**0.5  # Distance to centroid 1
data['g'] = ((data['x'] - cent2[0])**2 + (data['y'] - cent2[1])**2)**0.5  # Distance to centroid 2
data['b'] = ((data['x'] - cent3[0])**2 + (data['y'] - cent3[1])**2)**0.5  # Distance to centroid 3

# Assign each point to the nearest centroid
data['labels'] = data[['r', 'g', 'b']].idxmin(axis=1)
print(data[['x', 'y', 'labels']])
```

#### Step 3: Recalculate Centroids

For each cluster, compute the mean of all points assigned to it and update the centroid.

```python
cent1 = [data[data['labels'] == 'r']['x'].mean(), data[data['labels'] == 'r']['y'].mean()]
cent2 = [data[data['labels'] == 'g']['x'].mean(), data[data['labels'] == 'g']['y'].mean()]
cent3 = [data[data['labels'] == 'b']['x'].mean(), data[data['labels'] == 'b']['y'].mean()]
print("Updated centroids:", cent1, cent2, cent3)
```

#### Step 4: Repeat Steps 2 & 3

Continue the assignment and centroid update steps until the labels no longer change or a maximum number of iterations is reached.

---

## 6. Visualization of Clusters

After clustering, visualize the results:

```python
colors = {'r':'red', 'g':'green', 'b':'blue'}
plt.scatter(data['x'], data['y'], c=data['labels'].map(colors))
plt.scatter(cent1[0], cent1[1], c='red', marker='*', s=200, label='Centroid 1')
plt.scatter(cent2[0], cent2[1], c='green', marker='*', s=200, label='Centroid 2')
plt.scatter(cent3[0], cent3[1], c='blue', marker='*', s=200, label='Centroid 3')
plt.legend()
plt.title('Clustered Data with K-Means')
plt.show()
```

---

## 7. Significance and Analysis of Clusters

Once clusters are formed, analyze each for:
- **Size:** Number of points in each cluster.
- **Location:** Centroid coordinates.
- **Spread:** Variance within cluster.
- **Interpretation:** What does each cluster represent in context?

---

## Complete Example: K-Means in Python

```python
from sklearn.cluster import KMeans

# Prepare data
X = data[['x', 'y']]

# Fit K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
data['cluster'] = kmeans.fit_predict(X)

# Plot clusters
plt.scatter(data['x'], data['y'], c=data['cluster'])
plt.scatter(*zip(*kmeans.cluster_centers_), c=['red','green','blue'], marker='*', s=200)
plt.title('K-Means Clustering Example')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

---

## Summary

- **Unsupervised Learning** finds patterns in unlabelled data.
- **Clustering** groups similar data points.
- **K-Means** is an iterative algorithm for clustering, involving initialization, assignment, update, and convergence.
- **Visualization and Analysis** help interpret the results and the structure within the data.

---
