# Pandas: Data Manipulation and Analysis in Python

This document explains the concepts covered in the notebook `el_ds_2(pandas).ipynb`, focusing on the basics of the Pandas library, its comparison with Numpy, and hands-on examples of creating and manipulating Pandas data structures.

---

## 1. What is Pandas?

- **Pandas** is a powerful Python library for data manipulation and analysis.
- The name "Pandas" stands for "Panel Data".
- Built on top of **NumPy**, Pandas is especially popular in data science, machine learning, finance, and healthcare for handling structured data.

### Key Features

- Easy handling of missing data.
- Size mutability: columns can be inserted and deleted from DataFrame and higher dimensional objects.
- Automatic and explicit data alignment.
- Powerful, flexible group by functionality to perform split-apply-combine operations on data sets.
- High performance merging and joining of data.
- Hierarchical axis indexing for working with high-dimensional data in a lower-dimensional data structure.

---

## 2. Comparing Numpy and Pandas

| Aspect          | NumPy                             | Pandas                                     |
|-----------------|-----------------------------------|--------------------------------------------|
| **Purpose**     | Numerical computing               | Data analysis and manipulation             |
| **Data Structure** | `ndarray` (multi-dimensional array) | `Series` (1D), `DataFrame` (2D, like Excel) |
| **Data Type**   | Homogeneous (single type)         | Heterogeneous (mixed types allowed)        |
| **Speed**       | Faster for numeric computation    | Slightly slower, but more powerful for tables |

**Example Table:**
```python
import numpy as np
import pandas as pd

# Numpy array
np_array = np.array([[1, 2], [3, 4]])
print(np_array)
# Output:
# [[1 2]
#  [3 4]]

# Pandas DataFrame
df = pd.DataFrame({'A': [1, 3], 'B': [2, 4]})
print(df)
# Output:
#    A  B
# 0  1  2
# 1  3  4
```

---

## 3. Creating Data Structures in Pandas

### 3.1 Series (1D)

A **Series** is a one-dimensional array-like object containing an array of data and an associated array of labels, called its index.

```python
import pandas as pd

# Creating a Series
s = pd.Series([10, 20, 30, 40])
s.index = ['a', 'b', 'c', 'd']  # Label-based indexing
print(s)
# Output:
# a    10
# b    20
# c    30
# d    40
# dtype: int64
```
**Key Points:**
- Series is 1-dimensional and does **not** have columns, only an index and values.
- Trying to assign `.columns` to a Series will raise an error or be ignored.

**Accessing Elements:**
```python
print(s.loc['a'])  # Output: 10
print(type(s))     # Output: <class 'pandas.core.series.Series'>
```

---

### 3.2 DataFrame (2D)

A **DataFrame** is a two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).

**Creating a DataFrame from a Dictionary:**
```python
data = {
    'name': ['Jai', 'Ramesh', 'Pavan', 'Raj'],
    'age': [23, 24, 25, 26]
}
df = pd.DataFrame(data)
df.index = [1, 2, 3, 4]  # Custom index
print(df)
# Output:
#      name  age
# 1     Jai   23
# 2  Ramesh   24
# 3   Pavan   25
# 4     Raj   26
```

**Accessing DataFrame Columns:**
```python
print(df['name'][1])  # Output: Jai
```

**Creating a DataFrame from a Numpy Array:**
```python
import numpy as np

n1 = np.array([
    [2, 3, 1, 4],
    [3, 2, 1, 4],
    [4, 3, 7, 8],
    [9, 7, 4, 3],
    [2, 4, 5, 6]
])
df2 = pd.DataFrame(n1)
df2.columns = ['a', 'b', 'c', 'd']
print(df2)
# Output:
#    a  b  c  d
# 0  2  3  1  4
# 1  3  2  1  4
# 2  4  3  7  8
# 3  9  7  4  3
# 4  2  4  5  6
```

---

## 4. Summary of Concepts

- **Series:** One-dimensional, has index and values only, no columns.
- **DataFrame:** Two-dimensional, like a table, has rows and columns.
- **Data Types:** Series and DataFrames can hold different types of data (integers, strings, floats, etc.).
- **Indexing:** Both Series and DataFrames allow for custom indexing.

---

## 5. Common Mistakes

- Assigning `.columns` to a Series (invalid, only for DataFrames).
- Attempting to use mixed types within NumPy arrays (NumPy prefers single types; Pandas handles mixed types).

---

## 6. Practical Usage

Pandas is your go-to library for:

- Handling and cleaning data (missing values, duplicates).
- Analyzing tabular data (grouping, aggregating).
- Reading and writing data from various file formats (CSV, Excel, SQL, etc.).
- Preparing datasets for machine learning or statistical analysis.

---

## 7. Further Reading

- [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [NumPy vs Pandas: When to Use Which?](https://realpython.com/pandas-python-explore-dataset/)
- [10 Minutes to Pandas (Official Guide)](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)

---
