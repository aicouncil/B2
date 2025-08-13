# Detailed Explanation of `perceptron_model.ipynb`

This Jupyter Notebook demonstrates the basics of linear regression with a perceptron-like model using gradient descent, applied to the classic Advertising dataset. Below is a breakdown of the notebook content, definitions, examples, and use cases.

---

## 1. **Imports and Setup**

```python
import pandas as pd
import numpy as np
```

- **`pandas`**: Used for data manipulation and analysis, especially for reading and handling tabular data.
- **`numpy`**: Used for numerical computations, arrays, and mathematical operations.

---

## 2. **Loading the Dataset**

```python
df = pd.read_csv('https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/Advertising.csv', index_col=0)
df.head()
```

- **Dataset**: Advertising.csv contains data about advertising budgets (TV, radio, newspaper) and corresponding sales.
- **Columns**:
  - `TV`: Budget spent on TV ads.
  - `radio`: Budget spent on radio ads.
  - `newspaper`: Budget spent on newspaper ads.
  - `sales`: Sales generated.
- **Example**: Viewing the first five rows shows the relationship between advertising budgets and sales.

---

## 3. **Defining Features and Target**

```python
X = df[['TV', 'radio', 'newspaper']]
y = df['sales']
```

- **Features (`X`)**: TV, radio, and newspaper budgets.
- **Target (`y`)**: Sales.
- **Use Case**: Predict sales based on advertising budgets.

---

## 4. **Linear Model Definition**

```python
#Yh = w0 + w1X1 + w2X2 + w3X3

w0 = 1
w1 = 1
w2 = 1
w3 = 1

Yh = w0 + w1*X.TV + w2*X.radio + w3*X.newspaper
print(Yh)
```

- **Model Equation**:  
  \( Y_h = w_0 + w_1 \cdot X_{TV} + w_2 \cdot X_{radio} + w_3 \cdot X_{newspaper} \)
- **Weights (`w0`, `w1`, `w2`, `w3`)**: Initialized to 1.
- **Feed Forward**: Computes predicted sales (`Yh`) using current weights.
- **Use Case**: Initial prediction before training.

---

## 5. **Error Calculation**

```python
error = ((y - Yh)**2).mean()
print(error)
```

- **Error Metric**: Mean Squared Error (MSE).
  - Measures average squared difference between actual sales and predicted sales.
- **Purpose**: Quantifies the accuracy of the model.

---

## 6. **Gradient Descent Implementation**

```python
#Calculate gradient

w0 = 1
w1 = 1
w2 = 1
w3 = 1

for i in range(0,1000):
  Yh = w0 + w1*X.TV + w2*X.radio + w3*X.newspaper

  dew0 = -2*((y - Yh)).mean()
  dew1 = -2*((y - Yh)*X.TV).mean()
  dew2 = -2*((y - Yh)*X.radio).mean()
  dew3 = -2*((y - Yh)*X.newspaper).mean()

  lr = 1e-5

  w0 = w0 - lr * dew0
  w1 = w1 - lr * dew1
  w2 = w2 - lr * dew2
  w3 = w3 - lr * dew3

  error = ((y - Yh)**2).mean()
  print(i,error)
```

- **Gradient Descent**: Iteratively adjusts weights to minimize error.
- **Partial Derivatives (`dew0`, `dew1`, `dew2`, `dew3`)**:
  - Calculated with respect to each weight.
  - Used to determine the direction and magnitude of weight updates.
- **Learning Rate (`lr`)**: Controls step size for each update (set at `1e-5`).
- **Iterations**: Loop runs for 1000 epochs, printing the error at each step.
- **Purpose**: Trains the model to fit the data.

---

## 7. **Definitions & Concepts**

### **Perceptron**
- Originally a binary classifier, but generalized here as a linear regressor.
- Consists of input features, weights, and an output.

### **Gradient Descent**
- Optimization algorithm that minimizes a function (error) by iteratively moving in the direction of steepest descent as defined by the negative of the gradient.

### **Mean Squared Error (MSE)**
- Standard loss function for regression problems.

### **Weights**
- Parameters learned during training to best map inputs to outputs.

---

## 8. **Examples & Use Cases**

- **Example**: Predicting product sales based on advertising budgets.
- **Use Case**: Businesses can estimate the return on investment for different advertising channels.
- **Learning Process**: Shows how a model improves predictions by adjusting weights using gradient descent.
- **Educational Value**: Great introductory example for understanding both linear regression and the basics of neural network training.

---

## 9. **Summary**

This notebook provides a hands-on, step-by-step introduction to:
- Loading and exploring a regression dataset.
- Defining a linear model (perceptron-like).
- Calculating prediction error.
- Implementing and visualizing gradient descent for training.
- Learning how weights are updated to minimize prediction error.

**This foundational understanding is applicable to:**
- Linear regression for prediction tasks.
- Understanding the basics of neural networks (perceptrons).
- General machine learning workflows (data, model, loss, optimization).

---
