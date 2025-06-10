# Detailed Explanation: `el_ds_4(regression).ipynb`

This notebook provides a hands-on introduction to **regression analysis** using Python. The focus is on understanding simple linear regression both mathematically (by hand) and practically (using Scikit-learn). Below is a step-by-step breakdown of the content, explanations, and illustrative examples.

---

## 1. Introduction to Regression

**Regression** is a type of supervised machine learning used to predict a continuous numerical value based on input features. For example:
- Predicting salary based on years of experience.
- Predicting house price based on area, location, etc.

> **Goal**: Learn how to fit a line to data so you can predict new values.

---

## 2. Import Required Libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
- **numpy**: For numerical operations.
- **pandas**: For handling datasets.
- **matplotlib.pyplot**: For plotting data.

---

## 3. Sample Data Creation

A simple dataset is created with two columns:
- `yoe`: Years of experience
- `salary`: Salary (in arbitrary units)

```python
salary_data = pd.DataFrame({
    "yoe": [4, 6, 3, 8, 9, 7],
    "salary": [10, 14, 8, 14, 17, 11]
})
```

**Data Table:**

| yoe | salary |
|-----|--------|
| 4   | 10     |
| 6   | 14     |
| 3   | 8      |
| 8   | 14     |
| 9   | 17     |
| 7   | 11     |

---

## 4. Data Visualization

Scatter plot to visualize the relation between years of experience and salary:

```python
plt.scatter(salary_data['yoe'], salary_data['salary'])
plt.show()
```
**Explanation:**  
This plot helps visually assess if there is a linear relationship between the variables. Each point represents an employee's years of experience and their corresponding salary.

---

## 5. Linear Regression by Hand

### The Linear Model

The basic equation for linear regression:
> \( y = w_0 + w_1 \cdot x \)

Where:
- \( y \): Target value (salary)
- \( x \): Feature (years of experience)
- \( w_0 \): Intercept (where line crosses the y-axis)
- \( w_1 \): Slope (how much y changes for each unit change in x)

### Calculating Slope (\( w_1 \)) and Intercept (\( w_0 \)) Manually

```python
x = salary_data['yoe']
y = salary_data['salary']

n1 = ((x - x.mean()) * (y - y.mean())).sum()
d1 = ((x - x.mean())**2).sum()

w1 = n1 / d1
print(w1)  # Output: 1.2546583850931674

w0 = y.mean() - w1 * x.mean()
print(w0)  # Output: 4.596273291925468
```

#### **Explanation:**
- **Slope (\( w_1 \))**: Measures how much the salary increases for each additional year of experience.
- **Intercept (\( w_0 \))**: The predicted salary for 0 years of experience.

#### **Example Calculation:**
If someone has 5.5 years of experience:
```python
yoe = 5.5
predicted_salary = w0 + w1 * yoe
print(predicted_salary)  # Output: 11.50
```
So, an employee with 5.5 years of experience is predicted to have a salary of 11.5 units.

---

## 6. Visualizing the Regression Line

```python
yh = w0 + w1 * x

plt.scatter(x, y)               # Plot actual data points
plt.plot(x, yh, 'r')            # Plot regression line in red
plt.show()
```
**Explanation:**  
This plot shows both the actual data and the best-fit line calculated manually. The closeness of the data points to the line indicates how well the model fits the data.

---

## 7. Using Scikit-learn for Simple Linear Regression

Instead of calculating everything by hand, we can use the `LinearRegression` class from Scikit-learn.

```python
from sklearn.linear_model import LinearRegression

x = salary_data[['yoe']]  # Note: 2D array
y = salary_data['salary']

modelA = LinearRegression()
modelA.fit(x, y)
```

### **Explanation:**
- `modelA.fit(x, y)`: Finds the best fit line by learning the intercept and slope from the data.
- After fitting, you can use `modelA.predict(new_x)` to predict salary for new values of years of experience.

#### **Example:**
```python
pred_salary = modelA.predict([[5.5]])
print(pred_salary)
```
This will give the predicted salary for 5.5 years of experience using Scikit-learn's implementation.

---

## 8. Summary Table

| Step                       | By Hand                                   | Using Scikit-learn                        |
|----------------------------|--------------------------------------------|-------------------------------------------|
| Calculate parameters       | Use formulas to find w0 (intercept) and w1 (slope) | Call `model.fit(x, y)`                    |
| Make predictions           | `y_pred = w0 + w1 * x`                    | `model.predict(x)`                        |
| Visualize results          | Plot data and regression line manually     | Plot as above, or use built-in tools      |

---

## 9. Key Takeaways

- **Regression** helps predict continuous values.
- **Simple Linear Regression** finds a straight line that best fits the data.
- You can compute regression parameters (`w0`, `w1`) by hand for learning or use Scikit-learn for practical applications.
- Visualization is crucial to understand the fit and relationship.

---

## 10. Practice Example

Try predicting the salary for someone with 10 years of experience using both by-hand and Scikit-learn methods:

**By hand:**
```python
yoe = 10
predicted_salary = w0 + w1 * yoe
print(predicted_salary)
```

**With Scikit-learn:**
```python
pred_salary = modelA.predict([[10]])
print(pred_salary)
```

---

## 11. Further Learning

- Try adding more features (e.g., education, skill score) for **multiple linear regression**.
- Explore model evaluation metrics like **Mean Squared Error (MSE)** and **R² score**.
- Test on new, unseen data to see how well your regression generalizes.

---

**End of Explanation**
