# Univariate and Bivariate Analysis in Pandas

Data analysis in pandas often starts with **univariate** (single variable) and **bivariate** (two variables) exploration. This helps understand the data's structure, detect outliers, and uncover relationships between variables.

---

## 1. Univariate Analysis on Continuous Data Columns

Univariate analysis examines each variable separately to summarize and find patterns in the data.

### What are Continuous Data Columns?

- **Continuous variables** can take any value within a range, e.g., age, salary, height.
- They are usually numeric.

### Why Perform Univariate Analysis?

- Understand the distribution (normal, skewed, etc.)
- Detect outliers and errors
- Summarize data (mean, median, etc.)

### Key Techniques in Pandas

#### a. Descriptive Statistics

Use `.describe()` to see count, mean, std, min, max, and quartiles:

```python
df['Age'].describe()
```

**Example Output:**
```
count    891.000000
mean      29.699118
std       14.526497
min        0.420000
25%       20.125000
50%       28.000000
75%       38.000000
max       80.000000
```

#### b. Central Tendency and Spread

- **Mean:** `df['Age'].mean()`
- **Median:** `df['Age'].median()`
- **Mode:** `df['Age'].mode()`
- **Standard Deviation:** `df['Age'].std()`

#### c. Visualizing Distribution

- **Histogram:**
  ```python
  df['Age'].plot.hist(bins=20, edgecolor='k')
  ```
- **Boxplot:**
  ```python
  df['Age'].plot.box()
  ```

#### d. Skewness and Kurtosis

- **Skewness:** `df['Age'].skew()`
  - > 0: right-skewed; < 0: left-skewed
- **Kurtosis:** `df['Age'].kurt()`
  - > 0: heavy tails; < 0: light tails

#### e. Outlier Detection

```python
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Age'] < Q1 - 1.5 * IQR) | (df['Age'] > Q3 + 1.5 * IQR)]
print(outliers)
```

---

## 2. Bivariate Analysis in Pandas

Bivariate analysis explores the relationship between two variables. This can be between:

- Categorical and categorical
- Categorical and continuous
- Continuous and continuous

### a. Using `pd.crosstab()` for Categorical Variables

`pd.crosstab()` creates a frequency table (contingency table) for two categorical variables.

```python
pd.crosstab(df['Sex'], df['Survived'])
```

**Example Output:**
|Survived| 0 | 1 |
|--------|---|---|
|female  | 81|233|
|male    |468|109|

- Tells how many males/females survived or not.

### b. Using `.corr()` for Correlation Between Continuous Variables

`.corr()` computes the correlation matrix for numeric columns.

```python
df[['Age', 'Fare']].corr()
```

**Example Output:**
|      | Age   | Fare   |
|------|-------|--------|
|Age   |1.000  |-0.0969 |
|Fare  |-0.0969|1.000   |

- Correlation values close to 1 or -1 indicate strong relationships.

### c. Using `.groupby()` for Aggregated Statistics

`groupby()` groups data and computes aggregate statistics (mean, count, etc.) for each group.

```python
# Average fare by gender
df.groupby('Sex')['Fare'].mean()
```

**Example Output:**
|Sex   | Fare   |
|------|--------|
|female|44.479  |
|male  |25.523  |

- Useful for comparing continuous variables across categories.

### d. Visualizing Relationships

- **Bar plot for group means:**
  ```python
  df.groupby('Sex')['Fare'].mean().plot.bar()
  ```
- **Scatter plot for continuous variables:**
  ```python
  df.plot.scatter(x='Age', y='Fare')
  ```

---

## 3. Summary Table

| Function                  | Description                                        | Example Use                      |
|---------------------------|----------------------------------------------------|----------------------------------|
| `describe()`              | Summary stats for one column                       | `df['Age'].describe()`           |
| `plot.hist()`             | Distribution shape                                 | `df['Age'].plot.hist()`          |
| `plot.box()`              | Quartiles, outliers                                | `df['Age'].plot.box()`           |
| `skew()`, `kurt()`        | Shape of distribution                              | `df['Age'].skew()`               |
| `mean()`, `median()`      | Central tendency                                   | `df['Fare'].mean()`              |
| `pd.crosstab()`           | Frequency table for two categorical variables      | `pd.crosstab(df['Sex'], df['Survived'])` |
| `corr()`                  | Correlation between numeric columns                | `df.corr()`                      |
| `groupby()`               | Aggregate stats by group                           | `df.groupby('Sex')['Fare'].mean()`|
| `plot.scatter()`          | Relationship between two continuous variables      | `df.plot.scatter(x='Age', y='Fare')` |

---

## 4. Example Workflow in Pandas

```python
import pandas as pd
import matplotlib.pyplot as plt

# Univariate
print(df['Age'].describe())
df['Age'].plot.hist(bins=20)
plt.show()
df['Age'].plot.box()
plt.show()
print("Skewness:", df['Age'].skew())

# Bivariate
print(pd.crosstab(df['Sex'], df['Survived']))
print(df[['Age', 'Fare']].corr())
print(df.groupby('Sex')['Fare'].mean())
df.plot.scatter(x='Age', y='Fare')
plt.show()
```

---

## 5. Conclusion

- **Univariate analysis** is about understanding each variable individually.
- **Bivariate analysis** helps discover relationships between variables.
- Both are essential first steps in data exploration and should precede modeling or complex analytics.

---
