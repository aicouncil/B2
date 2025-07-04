# Variance Inflation Factor (VIF) Explained with Example

## What is VIF?

**Variance Inflation Factor (VIF)** is a measure used to detect multicollinearity in regression analysis.  
Multicollinearity occurs when independent variables (features) in a regression model are highly correlated with each other, which can make the model unstable and the coefficients unreliable.

- **VIF of 1:** No correlation among a variable and others.
- **VIF between 1-5:** Moderate correlation.
- **VIF > 5 (sometimes >10):** High correlation (problematic multicollinearity).

---

## How is VIF Calculated?

For each variable, VIF is calculated as:

```
VIF = 1 / (1 - R²)
```

Where R² is the coefficient of determination from regressing that variable against all others.

---

## Example: VIF Calculation on the Iris Dataset

#### 1. Importing Libraries and Data

```python
import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv('https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/Iris.csv')
```

#### 2. Selecting Features

The code selects the four numerical features from the Iris dataset:

```python
d1 = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
d1.insert(0, 'const', 1)  # Add constant for intercept
```

#### 3. Calculating VIF for Each Feature

```python
[variance_inflation_factor(d1.values, i) for i in range(d1.shape[1])]
```
- For each column in the DataFrame (including the constant), VIF is computed.

#### 4. Interpreting VIF in the Example

Suppose the VIF output is something like:
```
[15.23, 4.12, 1.43, 12.78, 9.65]
```
- The first value is for the constant and can be ignored.
- The other values correspond to: SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm.
- VIF values >5 or >10 indicate strong multicollinearity. For instance, if PetalLengthCm and PetalWidthCm have high VIF, they are highly correlated (as is visible from the correlation matrix).

#### 5. Why Does This Matter?

- **High VIF:** If you see a feature with a high VIF, it means that feature shares a lot of information with other features. This can make model coefficients unreliable.
- **Action:** You might consider removing or combining such features.

---

## Summary Example

Suppose you run:

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
d1 = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
d1.insert(0, 'const', 1)
vif = [variance_inflation_factor(d1.values, i) for i in range(d1.shape[1])]
print(vif)
```
- Output: `[12.3, 5.1, 1.2, 8.5, 9.7]`
- Interpretation: SepalLengthCm, PetalLengthCm, and PetalWidthCm have high VIF, suggesting multicollinearity issues mostly between them.

---

## Key Takeaways

- **VIF helps you detect multicollinearity.**
- **High VIF:** Consider feature engineering or dropping variables.
- **Low VIF:** No multicollinearity concern.

**In the Iris dataset example, VIF is used to check for collinearity among the main flower measurements, demonstrating both the calculation and its interpretation.**
