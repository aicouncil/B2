# Concepts Explained in `el_ds_3(pandas).ipynb`

This notebook demonstrates fundamental data analysis and manipulation techniques using the pandas library in Python, often applied to real-world datasets. Here’s a detailed explanation of the concepts, with examples and explanations:

---

## 1. Importing Required Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

**Explanation:**  
- `pandas` (pd): The primary data analysis library for tabular data in Python.
- `numpy` (np): Used for numerical operations, arrays, and mathematics.
- `matplotlib.pyplot` (plt): For plotting graphs and visualizations.

---

## 2. Loading a Dataset

```python
df = pd.read_csv('https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/Big_Mart_Sales_Figure.csv')
df.head()
```

**Explanation:**  
- `pd.read_csv()`: Loads data from a CSV file (here, from a URL).
- `df.head()`: Shows the first 5 rows of the DataFrame for a quick look at the data.

**Example Output Table:**

| Item_Identifier | Item_Weight | Item_Fat_Content | ... | Item_Outlet_Sales |
|-----------------|-------------|------------------|-----|-------------------|
| FDA15           | 9.30        | Low Fat          | ... | 3735.1380         |
| DRC01           | 5.92        | Regular          | ... | 443.4228          |
| ...             | ...         | ...              | ... | ...               |

---

## 3. Checking the Shape of Data

```python
df.shape
```

**Explanation:**  
- Returns a tuple `(rows, columns)` representing the number of rows and columns.
- Example output: `(8523, 12)` means 8,523 rows and 12 columns.

---

## 4. Checking Data Types

```python
df.dtypes
```

**Explanation:**  
- Provides the data type of each column.
- Helps identify numerical, categorical, and other data types to decide further processing.

**Example Output:**

| Column                    | Type    |
|---------------------------|---------|
| Item_Identifier           | object  |
| Item_Weight               | float64 |
| Item_Fat_Content          | object  |
| ...                       | ...     |
| Item_Outlet_Sales         | float64 |

---

## 5. Unique Values in Each Column

```python
df.nunique()
```

**Explanation:**  
- Gives the count of unique values for each column.
- Useful for understanding categorical vs. continuous data and feature cardinality.

**Example:**
- Item_Identifier: 1559 unique values
- Item_Type: 16 unique values
- Outlet_Identifier: 10 unique values

---

## 6. Separating Numerical and Non-Numerical Data

### Numerical Data

```python
df_num = df.select_dtypes(include='number')
df_num.head()
```

**Explanation:**  
- `select_dtypes(include='number')`: Selects only the columns with numeric data types (e.g., float, int).
- Useful for statistical analysis, correlation, and plotting distributions.

**Example Output (first 5 rows):**

| Item_Weight | Item_Visibility | Item_MRP | Outlet_Establishment_Year | Item_Outlet_Sales |
|-------------|-----------------|----------|--------------------------|-------------------|
| 9.30        | 0.016047        | 249.8092 | 1999                     | 3735.1380         |
| ...         | ...             | ...      | ...                      | ...               |

---

### Non-Numerical Data

```python
df_non_num = df.select_dtypes(exclude='number')
df_non_num.head()
```

**Explanation:**  
- `select_dtypes(exclude='number')`: Selects only the columns with non-numeric data types (e.g., object, category).
- Useful for encoding, one-hot encoding, and analyzing categorical features.

**Example Output (first 5 rows):**

| Item_Identifier | Item_Fat_Content | Item_Type | Outlet_Identifier | Outlet_Size | Outlet_Location_Type | Outlet_Type |
|-----------------|------------------|-----------|-------------------|-------------|---------------------|-------------|
| FDA15           | Low Fat          | Dairy     | OUT049            | Medium      | Tier 1              | Supermarket Type1 |
| ...             | ...              | ...       | ...               | ...         | ...                 | ...         |

---

## 7. General Workflow Demonstrated

1. **Import libraries**: Ensures all required packages are available.
2. **Load dataset**: Ingest real-world data for analysis.
3. **Inspect data**: Use `.head()`, `.shape`, `.dtypes`, and `.nunique()` to understand the dataset.
4. **Separate features**: Distinguish between numerical and categorical columns for targeted analysis.

---

## Practical Applications

- **Preprocessing**: Before modeling, separating numerical and categorical columns helps apply suitable preprocessing (e.g., scaling for numbers, encoding for categories).
- **Exploratory Data Analysis (EDA)**: Knowing the types, distribution, and uniqueness of data aids in data cleaning, feature engineering, and visualization.
- **Data Cleaning**: Understanding data types and uniqueness helps in detecting anomalies/missing values.

---

## Example Use Case

Suppose you need to build a sales prediction model using the Big Mart Sales data:
- Start by loading and inspecting the data (as above).
- Separate numerical columns to compute statistics such as mean sales, median item weight, etc.
- Separate categorical columns for encoding (e.g., converting "Outlet_Type" into numerical codes for modeling).
- Analyze unique values to decide if columns need to be merged or if high-cardinality columns need special treatment.

---

## Summary Table of Key Pandas Functions Used

| Function                          | Purpose                                  |
|------------------------------------|------------------------------------------|
| `pd.read_csv()`                    | Read a CSV file into a DataFrame         |
| `df.head()`                        | Shows the first n rows of the DataFrame  |
| `df.shape`                         | Returns the (rows, columns) tuple        |
| `df.dtypes`                        | Lists the data types for each column     |
| `df.nunique()`                     | Counts unique values per column          |
| `df.select_dtypes(include='number')`| Selects only numerical columns           |
| `df.select_dtypes(exclude='number')`| Selects only non-numerical columns       |

---

## Conclusion

The notebook covers the essential steps of data exploration and preprocessing in pandas, forming the foundation for advanced data analysis and machine learning workflows. Each of these steps is a standard best practice for any data scientist or analyst working with tabular data in Python.
