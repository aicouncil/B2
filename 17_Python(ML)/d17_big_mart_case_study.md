# Data Preprocessing in Regression: Skewed Data, Scaling, and R-Squared

This guide explains three fundamental concepts in regression analysis and machine learning data preprocessing:

1. **Converting Skewed Data to Normal Distribution**
2. **Data Scaling (Standardization/Normalization) and Its Effect on Coefficients**
3. **R-squared (Coefficient of Determination) for Model Evaluation**

---

## 1. Converting Skewed Data to Normally Distributed Data

### What is Skewed Data?

**Skewed data** occurs when the distribution of a variable is not symmetrical. Often, real-world data (like sales, incomes) are **right-skewed** (long tail to the right).

- **Why does it matter?**  
  Many statistical models (including linear regression) assume that data, especially the residuals, are **normally distributed**. Skewed data can lead to poor predictions and unreliable statistical inferences.

### Log Transformation

A common method to reduce skewness is to apply a **logarithmic transformation**:

```python
import numpy as np
Ylog = np.log(y)
```
- Here, `y` is the original data (e.g., a column of sales).
- `Ylog` is the transformed data, now closer to a normal distribution.

> **Note:** Log transformations only work with positive values. For data with zero or negative values, use `np.log1p(y)` or shift the data.

#### Example

Suppose your target variable is `Item_Outlet_Sales`:

```python
Ylog = np.log(df['Item_Outlet_Sales'])
```

#### Visualizing the Effect

```python
import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.hist(df['Item_Outlet_Sales'], bins=30)
plt.title('Original')

plt.subplot(1,2,2)
plt.hist(np.log(df['Item_Outlet_Sales']), bins=30)
plt.title('Log-Transformed')

plt.show()
```

- The log-transformed histogram will appear more symmetric and bell-shaped.

---

## 2. Data Scaling and Its Effect on Regression Coefficients

### Why Scale Data?

Features in your dataset may have widely varying ranges (e.g., weights in kg vs. prices in rupees). Models like linear regression are sensitive to the scale of features:
- Features with larger ranges can dominate the model.
- Coefficients become hard to interpret and compare.

### Common Scaling Techniques

- **Standardization (Z-score):**  
  Transforms data to have zero mean and unit variance.
  ```python
  from sklearn.preprocessing import StandardScaler
  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(X)
  ```
- **Min-Max Scaling:**  
  Scales data to a [0, 1] range.
  ```python
  from sklearn.preprocessing import MinMaxScaler
  scaler = MinMaxScaler()
  X_scaled = scaler.fit_transform(X)
  ```

### Effect on Regression Coefficients

- **Without scaling:** Coefficients depend on feature units and scales, making it hard to judge which feature matters most.
- **With scaling:** All features contribute equally, and you can directly compare coefficients to assess importance.

#### Example

If `Item_Weight` is in kg (range 5–20) and `Item_MRP` is in rupees (range 30–300), their raw coefficients are not comparable. After standardization, a coefficient of 0.5 for `Item_Weight` and 0.2 for `Item_MRP` means `Item_Weight` is more influential (in terms of standard deviations).

---

## 3. R-squared (Coefficient of Determination)

### What is R-squared?

**R-squared (R²)** is a metric that quantifies how much of the variability in the target variable can be explained by the linear model.

#### Formula

\[
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
\]
- \(SS_{res}\): Sum of squared residuals (differences between actual and predicted values)
- \(SS_{tot}\): Total sum of squares (differences between actual values and the mean)

#### Interpretation

- **R² = 1:** Model explains all variability (perfect fit).
- **R² = 0:** Model explains none of the variability.
- **R² < 0:** Model fits worse than predicting the mean.

#### Example in Python

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print("R-squared:", r2)
```

- **High R²**: Good fit.  
- **Low R²**: Poor fit.

---

## Sequenced Workflow Example

1. **Check Skewness**
   - Visualize with a histogram.
   - If skewed, apply a log transformation.

2. **Scale Features**
   - Use `StandardScaler` or `MinMaxScaler` to bring all features to a comparable range.

3. **Fit the Model**
   - Apply regression.

4. **Interpret Coefficients**
   - If features are scaled, coefficients can be directly compared for importance.

5. **Evaluate Model with R-squared**
   - Use R² to assess how well your model explains the data.

---

## Summary Table

| Concept        | What It Does                                       | Why It Matters                                                |
|----------------|----------------------------------------------------|---------------------------------------------------------------|
| Log Transform  | Reduces skewness, normalizes distribution          | Makes data suitable for models assuming normality             |
| Data Scaling   | Standardizes feature scales                        | Allows fair comparison of coefficients, improves convergence  |
| R-squared      | Measures variance explained by the model           | Evaluates model performance and fit                           |

---

**In summary:**  
- Convert skewed data to normal using log transforms.
- Scale features before regression for fair interpretation.
- Use R-squared to measure model effectiveness.

For further details and code examples, see the [notebook here](https://github.com/aicouncil/B2/blob/80778ca0876ecdfcbd1e8004cd88172bb2958e07/17_Python(ML)/el_ds_3(pandas).ipynb).
