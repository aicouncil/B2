# Insurance Case Study: Data Science Notebook Topics

This document explains the topics covered in the notebook `el_ds_11_Insurance_case_study.ipynb`, with examples to help you understand each step in the health insurance lead prediction workflow. The focus is on EDA (Exploratory Data Analysis) and basic data preprocessing using Python.

---

## 1. Importing Libraries

Before working with data, relevant Python libraries are imported:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `matplotlib.pyplot`: For data visualization.

---

## 2. Loading and Inspecting Data

The dataset is loaded from a CSV file into a pandas DataFrame. You can load a remote dataset directly as shown:

```python
df = pd.read_csv('https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/Health%20Insurance%20Lead%20Prediction%20Raw%20Data.csv')
df.head()
```

**Example Output:**

| ID | City_Code | Region_Code | Accomodation_Type | Reco_Insurance_Type | Upper_Age | Lower_Age | Is_Spouse | Health Indicator | Holding_Policy_Duration | Holding_Policy_Type | Reco_Policy_Cat | Reco_Policy_Premium | Response |
|----|-----------|-------------|-------------------|---------------------|-----------|-----------|-----------|------------------|------------------------|---------------------|------------------|---------------------|----------|
| 1  | C3        | 3213        | Rented            | Individual          | 36        | 36        | No        | X1               | 14+                    | 3.0                 | 22               | 11628.0             | 0        |
| 2  | C5        | 1117        | Owned             | Joint               | 75        | 22        | No        | X2               | NaN                    | NaN                 | 22               | 30510.0             | 0        |

---

## 3. Exploring Dataset Dimensions

Determine the size of your dataset using `.shape`:

```python
df.shape
```

**Example Output:**

```
(50882, 14)
```

- 50,882 rows (samples)
- 14 columns (features)

---

## 4. Data Preprocessing

### Dropping Unnecessary Columns

IDs are often irrelevant for modeling, so they are dropped:

```python
df1 = df.drop(columns=['ID'])
df1.head()
```

**After dropping `ID`, your columns are:**
- City_Code, Region_Code, Accomodation_Type, etc.

---

## 5. Data Types Exploration

It’s important to know which columns are numerical, categorical, or have other types:

```python
df.dtypes
```

**Example Output:**

| Column                  | Data Type |
|-------------------------|-----------|
| ID                      | int64     |
| City_Code               | object    |
| Region_Code             | int64     |
| Accomodation_Type       | object    |
| Reco_Insurance_Type     | object    |
| Upper_Age               | int64     |
| Lower_Age               | int64     |
| Is_Spouse               | object    |
| Health Indicator        | object    |
| Holding_Policy_Duration | object    |
| Holding_Policy_Type     | float64   |
| Reco_Policy_Cat         | int64     |
| Reco_Policy_Premium     | float64   |
| Response                | int64     |

- **int64/float64**: Numeric columns (suitable for calculations).
- **object**: Usually categorical or string data.

---

## 6. Analyzing Missing Data

Check for missing values in each column:

```python
df1.isna().sum() / len(df1)
```

**Example Output:**

| Column                  | Fraction of Missing Values |
|-------------------------|---------------------------|
| City_Code               | 0.000000                  |
| Region_Code             | 0.000000                  |
| Accomodation_Type       | 0.000000                  |
| Reco_Insurance_Type     | 0.000000                  |
| Upper_Age               | 0.000000                  |
| Lower_Age               | 0.000000                  |
| Is_Spouse               | 0.000000                  |
| Health Indicator        | 0.229767                  |
| Holding_Policy_Duration | 0.397999                  |
| Holding_Policy_Type     | 0.397999                  |
| Reco_Policy_Cat         | 0.000000                  |
| Reco_Policy_Premium     | 0.000000                  |
| Response                | 0.000000                  |

- Columns like **Health Indicator**, **Holding_Policy_Duration**, and **Holding_Policy_Type** have significant missing values.

---

## 7. Visualizing and Summarizing Data (Optional Next Steps)

While not shown in the extracted cells, it's common to continue with:

- **Summary statistics**:
    ```python
    df1.describe()
    ```

- **Visualizations**:
    ```python
    df1['Reco_Policy_Premium'].hist()
    plt.title("Distribution of Policy Premiums")
    plt.show()
    ```

---

## 8. Summary

**Topics Covered:**
- Loading data from remote CSV using pandas
- Inspecting first few rows with `.head()`
- Checking the dataset shape (`.shape`)
- Dropping irrelevant columns (`.drop()`)
- Checking data types (`.dtypes`)
- Identifying missing values (`.isna().sum()`)
- Understanding which columns are categorical, numerical, or have missing data

**These steps form the basis of any machine learning or data science case study, especially for structured data such as insurance leads.**

---

## Example: Full Workflow

```python
import pandas as pd

# Load data
df = pd.read_csv('data.csv')  # Use your CSV path

# Inspect data
print(df.head())
print(df.shape)

# Drop irrelevant columns
df1 = df.drop(columns=['ID'])

# Check data types
print(df1.dtypes)

# Find missing values
print(df1.isna().sum() / len(df1))
```

---

## Next Steps

Once the data is cleaned and understood, you can proceed to:
- Exploratory data analysis (EDA)
- Feature engineering
- Model training and evaluation

---

_This guide is based on the code and workflow from `el_ds_11_Insurance_case_study.ipynb`, part of the [aicouncil/B2](https://github.com/aicouncil/B2) repository._
