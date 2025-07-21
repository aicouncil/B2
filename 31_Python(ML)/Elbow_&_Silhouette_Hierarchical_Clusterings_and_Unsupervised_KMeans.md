# Elbow & Silhoutte

## Elbow Method

The elbow method is a technique used in k-means clustering to determine the optimal number of clusters (k). The basic idea is to run k-means clustering on the dataset for a range of values of k (e.g., from 1 to 10), and for each value of k, calculate the **Within-Cluster Sum of Squares (WCSS)**. Then, plot the curve of WCSS vs. the number of clusters. The location of a bend (knee) in the plot is generally considered as an indicator of the appropriate number of clusters.

```python
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
```

## Silhouette Score

The silhouette score is a metric used to calculate the quality of a clustering. It measures how similar a point is to its own cluster (cohesion) compared to other clusters (separation). The score ranges from -1 to 1.

- **+1**: means the sample is far away from the neighboring clusters.
- **0**: means the sample is on or very close to the decision boundary between two neighboring clusters.
- **-1**: means the sample might have been assigned to the wrong cluster.

```python
from sklearn.metrics import silhouette_score

for n_cluster in range(2, 11):
    kmeans = KMeans(n_clusters=n_cluster).fit(X)
    label = kmeans.labels_
    sil_coeff = silhouette_score(X, label, metric='euclidean')
    print(f"For n_clusters={n_cluster}, The Silhouette Coefficient is {sil_coeff}")
```

---

# Hierarachial Clusterings

## Dendrogram and Agglomerative Clustering

Hierarchical clustering builds nested clusters by either a **bottom-up** (agglomerative) or **top-down** (divisive) approach.

Agglomerative is more common:
1. Start with each data point as its own cluster.
2. Merge the closest pair of clusters.
3. Repeat until all data is in one single cluster.

The process is visualized using a dendrogram.

```python
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title("Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()
```

## Agglomerative Clustering using sklearn

```python
from sklearn.cluster import AgglomerativeClustering

hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(X)

print(y_hc)
```

## Visualizing Clusters

```python
import matplotlib.pyplot as plt

plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s=100, c='green', label='Cluster 3')
plt.title('Hierarchical Clustering')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
```

---

# Unsupervised KMeans

## What is KMeans Clustering?

KMeans is a type of unsupervised learning algorithm used for clustering. It partitions the dataset into K clusters by:

1. Initializing K centroids randomly.
2. Assigning each point to the closest centroid.
3. Updating centroids as the mean of points in each cluster.
4. Repeating steps 2 and 3 until convergence.

## Example with Iris Dataset

```python
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

print(y_kmeans)
```

## Visualizing KMeans Clusters

```python
import matplotlib.pyplot as plt

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')

plt.title('Clusters of Iris')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
```

## Conclusion

- Use **Elbow Method** to decide the best number of clusters by checking the inflection point of WCSS.
- Use **Silhouette Score** to validate the quality of clustering.
- **KMeans** is simple and fast for large datasets.
- **Hierarchical clustering** is good for small datasets and gives a full tree-based structure of cluster merging.
