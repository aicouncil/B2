# Gradient Descent & Lasso Regression: Combined Explanation with Code and Examples

---

## 🔍 The Goal of Any ML Regression Model

The core purpose of a regression model is **to predict a target variable (Y)** by learning the best relationship with input features (X) using a function like:

\[
\hat{y} = w_0 + w_1 x_1 + w_2 x_2 + ... + w_n x_n
\]

We aim to find the **optimal weights (w)** such that the error between predicted (\(\hat{y}\)) and actual (y) values is minimized.

---

## 1️⃣ Gradient Descent – The Optimization Engine

### 🚀 What It Does

- Gradient Descent is an **optimization algorithm** used to minimize the error (loss) of the model.
- It **adjusts model weights** based on the slope (gradient) of the loss curve.

### 🔁 Update Rule

\[
w = w - \alpha \cdot \frac{\partial E}{\partial w}
\]

Where:
- \( w \): Weight (parameter)
- \( \alpha \): Learning Rate (step size)
- \( \frac{\partial E}{\partial w} \): Gradient (partial derivative of error with respect to weight)

---

### 🧪 Example: Linear Regression Using Gradient Descent

```python
# Dataset
X = df['YearsExperience']
y = df['Salary']

# Initialization
w0, w1 = 1, 1

# Training loop
for i in range(5000):
    yh = w0 + w1 * X
    error = ((y - yh)**2).mean()

    # Gradient calculation
    dew0 = -2 * (y - yh).mean()
    dew1 = -2 * ((y - yh) * X).mean()

    # Update weights
    lr = 1e-2
    w0 -= lr * dew0
    w1 -= lr * dew1

print(w0, w1)
```

✅ This code uses gradient descent to find the best weights (`w0`, `w1`) that minimize **Mean Squared Error (MSE)**.

---

## 2️⃣ Lasso Regression – Regularized Linear Regression

### 🎯 What It Does

- Lasso Regression **adds a penalty** to the standard linear regression loss.
- The penalty is based on the **absolute value of coefficients (L1 norm)**:

\[
\text{Loss} = \text{MSE} + \alpha \cdot \sum |w_i|
\]

- This is called **L1 Regularization**.
- It shrinks less important feature weights toward zero, performing **automatic feature selection**.

---

### ⚙️ Lasso Uses Gradient Descent Too!

- Under the hood, Lasso also uses **gradient descent** to optimize weights, with the L1 penalty included in the loss function.

---

### 🧪 Example: Lasso Regression in Scikit-learn

```python
from sklearn.linear_model import Lasso
model_lasso = Lasso(alpha=0.01)
model_lasso.fit(xtrain_l, ytrain_l)

print(model_lasso.coef_)
```

**📉 Output Coefficients Example:**

| Feature                        | Coefficient |
|---------------------------------|-------------|
| Item_MRP                        | 1.82        |
| Outlet_Type_Grocery Store       | -1.85       |
| Outlet_Type_Supermarket Type1   | 0.00 ← Dropped |
| Outlet_Type_Supermarket Type2   | -0.079      |
| Outlet_Type_Supermarket Type3   | 0.453       |

✅ Lasso **automatically eliminates less useful features** by making their coefficients zero.

---

## 🔁 Combined View: What Happens During Training

| Step                | Gradient Descent         | Lasso Regression                |
|---------------------|-------------------------|---------------------------------|
| Loss Function       | MSE                     | MSE + L1 penalty (absolute weights) |
| Optimization        | Gradient Descent        | Gradient Descent (with L1)      |
| Weight Updates      | Using gradients         | Gradients + shrinkage           |
| Feature Selection   | ❌ Not possible         | ✅ Sets some weights to 0        |
| Used In             | Linear/Logistic Reg., NN| Regularized Linear Models       |

---

## 📊 Visual Analogy

- **Gradient Descent:** Like rolling down a hill to reach the lowest point (minimum error).
- **Lasso:** Adds a "wall" along the way, forcing the path to ignore unimportant dimensions (features) by setting their weights to zero.

---

## ✅ When to Use What?

| Scenario                                     | Use                       |
|-----------------------------------------------|---------------------------|
| Reduce overfitting & simplify model           | ✅ Lasso                  |
| Only minimize prediction error                | Gradient Descent          |
| Deep learning or neural network training      | Gradient Descent          |
| Feature selection in regression problems      | ✅ Lasso                  |

---

## 🎯 Final Summary

| Concept             | Gradient Descent         | Lasso Regression (L1)              |
|---------------------|-------------------------|------------------------------------|
| Main Use            | Minimize loss (MSE, etc)| Reduce loss & eliminate features   |
| Includes penalty?   | ❌ No                   | ✅ Yes (adds L1 penalty)           |
| Shrinks weights?    | ❌ Only if loss needs   | ✅ Drives small/irrelevant weights to zero |
| Technique           | Weight updates by grads | Same, + shrinkage logic            |
| Key Benefit         | Learns best-fit line    | Best-fit + simpler (sparse) model  |

---

> **In essence:**  
> - **Gradient Descent** is the universal optimizer for minimizing errors in ML models.
> - **Lasso Regression** is a special case that uses gradient descent, but with L1 penalty, helping in **feature selection** and improved generalization.
