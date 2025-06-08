## Handling Missing Values in Pandas

Dealing with missing values is a crucial step in data cleaning and preparation. Pandas provides a suite of easy and powerful tools to detect, remove, and fill missing (NaN) values in your datasets.

### 1. **Detecting Missing Values**

- **`isnull()` and `notnull()`**

  These functions are used to detect missing values in DataFrames or Series. They return a boolean mask.

  ```python
  import pandas as pd

  df = pd.DataFrame({
      'A': [1, 2, None],
      'B': [4, None, 6]
  })
  print(df.isnull())
  ```
  **Output:**
  ```
       A      B
  0  False  False
  1  False   True
  2   True  False
  ```

- **`isna()`** is an alias for `isnull()`.

### 2. **Removing Missing Values**

- **`dropna()`** removes any rows (or columns) with missing values.

  ```python
  # Remove rows with any missing values
  cleaned_df = df.dropna()
  print(cleaned_df)
  ```
  **Output:**
  ```
     A    B
  0  1.0  4.0
  ```

  - To remove columns with missing values: `df.dropna(axis=1)`

### 3. **Filling Missing Values**

- **`fillna()`** replaces missing values with a specified value or method.

  ```python
  # Replace all NaN with 0
  filled_df = df.fillna(0)
  print(filled_df)
  ```
  **Output:**
  ```
     A    B
  0  1.0  4.0
  1  2.0  0.0
  2  0.0  6.0
  ```

  - You can also use statistical values:
    ```python
    # Fill missing with the mean of the column
    df['A'].fillna(df['A'].mean(), inplace=True)
    ```
  - **Forward-fill** and **backward-fill** methods:
    ```python
    df.fillna(method='ffill')  # Propagates last valid observation forward
    df.fillna(method='bfill')  # Uses next valid observation to fill gap
    ```

### 4. **Example with Real Data**

Suppose you have a retail dataset with some `NaN` values in the `Outlet_Size` column:

```python
import pandas as pd

data = {
    'Item_Identifier': ['FDA15', 'DRC01', 'FDN15', 'FDX07', 'NC'],
    'Outlet_Size': ['Medium', 'High', None, 'Small', None]
}
df = pd.DataFrame(data)
print(df)
```
**Output:**
```
  Item_Identifier Outlet_Size
0           FDA15      Medium
1           DRC01        High
2           FDN15        None
3           FDX07       Small
4              NC        None
```

- **Detect missing values:**
  ```python
  print(df['Outlet_Size'].isnull())
  ```
  **Output:**
  ```
  0    False
  1    False
  2     True
  3    False
  4     True
  Name: Outlet_Size, dtype: bool
  ```

- **Fill missing values with a default (e.g., 'Medium'):**
  ```python
  df['Outlet_Size'].fillna('Medium', inplace=True)
  print(df)
  ```
  **Output:**
  ```
    Item_Identifier Outlet_Size
  0           FDA15      Medium
  1           DRC01        High
  2           FDN15      Medium
  3           FDX07       Small
  4              NC      Medium
  ```

### 5. **Best Practices & Tips**

- Always inspect your data with `isnull().sum()` to see the count of missing values per column.
- Decide whether to drop or fill missing values based on the context and importance of the data.
- Forward/backward filling (`ffill`, `bfill`) is useful for time series data.
- For categorical columns, filling with the mode (most frequent value) is common.
- For numerical columns, filling with mean or median is standard.

---

**Summary Table**

| Function              | Description                               | Example Use                          |
|-----------------------|-------------------------------------------|--------------------------------------|
| `isnull()`/`isna()`   | Detect missing values                     | `df.isnull().sum()`                  |
| `dropna()`            | Remove rows/columns with missing values   | `df.dropna(axis=0)`                  |
| `fillna()`            | Fill missing values                       | `df.fillna(0)`                       |

---

**References & More Details:**
- [Pandas Documentation on Missing Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)

You can find more details and code examples by browsing the [source notebook here](https://github.com/aicouncil/B2/blob/main/11_Python%28Pandas%29/el_ds_2%28pandas%29.ipynb).

---
*Note: The above explanation is based on standard Pandas practices and the structure of your repository. If you want examples from a specific dataset in your notebook, please specify the dataset name or share the relevant cell's content!*
