# Non-Linear Regression: Detailed Explanation and Examples

This document explains the topics and code covered in the notebook **el_ds_4(non_linear_regression).ipynb**, focusing on how non-linear regression can be performed using polynomial features with linear regression models in Python.

---

## Table of Contents

1. [Introduction to Non-Linear Regression](#introduction)
2. [Dataset Used](#dataset)
3. [Feature Engineering: Creating Polynomial Features](#feature-engineering)
4. [Fitting a Non-Linear Regression Model](#fitting-model)
5. [Summary](#summary)

---

<a name="introduction"></a>
## 1. Introduction to Non-Linear Regression

**Linear regression** assumes a straight-line relationship between the input variables (features) and the output variable (target). However, many real-world relationships are non-linear.

**Non-linear regression** is used when the relationship between variables appears to be curved or more complex than a straight line. One common approach to handle non-linearity is to transform the input features into polynomial features (e.g., squares, cubes) and then use linear regression on these transformed features. This effectively fits a polynomial curve to the data.

---

<a name="dataset"></a>
## 2. Dataset Used

The code starts by creating a simple dataset representing years of experience (`yoe`) and the corresponding salary (`salary`):

```python
import pandas as pd

salary_data = pd.DataFrame({
    "yoe": [4, 6, 3, 8, 9, 7],
    "salary": [10, 14, 8, 14, 17, 11]
})

print(salary_data)
```

**Output:**

| yoe | salary |
|-----|--------|
|  4  |   10   |
|  6  |   14   |
|  3  |    8   |
|  8  |   14   |
|  9  |   17   |
|  7  |   11   |

- `yoe`: Years of Experience
- `salary`: Salary in some units (say, lakhs per annum)

---

<a name="feature-engineering"></a>
## 3. Feature Engineering: Creating Polynomial Features

To fit a non-linear relationship, we expand the feature set by creating polynomial terms (squared and cubed):

```python
x = salary_data[['yoe']]
y = salary_data['salary']

# Create polynomial features: x, x^2, x^3
X_new = pd.concat((x, x**2, x**3), axis=1)
X_new.columns = ['yoe', 'yoe_squared', 'yoe_cube']

print(X_new)
```

**Output:**

| yoe | yoe_squared | yoe_cube |
|-----|-------------|----------|
|  4  |     16      |    64    |
|  6  |     36      |   216    |
|  3  |      9      |    27    |
|  8  |     64      |   512    |
|  9  |     81      |   729    |
|  7  |     49      |   343    |

**Explanation:**  
For each value of `yoe`, we create a new feature for `yoe^2` and `yoe^3`. This allows the model to fit more complex, curved relationships, not just straight lines.

**General Formula:**
If `y` is the salary and `x` is years of experience:
```
y = b0 + b1*x + b2*x^2 + b3*x^3 + error
```
Where `b0`, `b1`, `b2`, and `b3` are coefficients learned by the regression model.

---

<a name="fitting-model"></a>
## 4. Fitting a Non-Linear Regression Model

Now, we use the expanded feature set to fit a linear regression model. While the model itself is linear in terms of the coefficients, the use of polynomial features allows it to fit non-linear relationships.

```python
from sklearn.linear_model import LinearRegression

model_non_linear = LinearRegression()
model_non_linear.fit(X_new, y)
```

**Explanation:**  
- We use `LinearRegression` from `sklearn`, but fit it on polynomial features.
- The model learns the best coefficients for each term (`yoe`, `yoe_squared`, `yoe_cube`) to predict salary.

**Why this works:**  
The model is still a linear regression model, but since the input features now include powers of `yoe`, the predictions will follow a polynomial curve, allowing us to model complex, non-linear trends.

---

### Example: Making Predictions

Suppose we want to predict the salary for someone with 5 years of experience:

```python
import numpy as np

# Prepare the input for 5 years of experience
x_input = np.array([[5]])
x_input_poly = np.concatenate([x_input, x_input**2, x_input**3], axis=1)

# Predict using the trained model
salary_pred = model_non_linear.predict(x_input_poly)
print("Predicted salary for 5 years of experience:", salary_pred[0])
```

---

### Visualizing the Fit

To better understand how the polynomial regression fits the data, we can plot the original data points and the fitted curve.

```python
# Generate a sequence of values for x (years of experience)
x_range = np.linspace(min(x['yoe']), max(x['yoe']), 100).reshape(-1, 1)
x_range_poly = np.concatenate([x_range, x_range**2, x_range**3], axis=1)

# Predict salaries for this range
y_pred = model_non_linear.predict(x_range_poly)

# Plot
plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x_range, y_pred, color='red', label='Polynomial fit')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Non-Linear Regression (Polynomial Features)')
plt.legend()
plt.show()
```

---

<a name="summary"></a>
## 5. Summary

- **Non-linear regression** can be achieved by transforming the input features into polynomial features.
- **LinearRegression** can fit these features to model complex, curved relationships.
- This approach is simple yet powerful for capturing non-linear trends in data.

**Key Takeaway:**  
Polynomial feature engineering allows us to use linear models for non-linear relationships, making them a versatile tool in machine learning.

---

## Further Reading

- [Scikit-learn: Polynomial regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)
- [Non-linear regression in Python](https://machinelearningmastery.com/polynomial-regression-for-predicting-sales/)
