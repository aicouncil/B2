# Fundamentals of Neural Networks: A Manual Feedforward Example

This document provides a detailed explanation of the `perceptron_model.py` script, which illustrates the foundational concepts of a linear regression model's feedforward process. The script manually defines a model and calculates its initial prediction and error, providing a conceptual understanding of how a simple neural network or perceptron operates before training begins.

## 1. Project Context and Data Loading

* **Goal:** The script's implicit goal is to demonstrate the first step of building a predictive model to estimate property sales based on advertising costs. The model is a form of multi-variable linear regression.
* **Data Loading:** The script uses `pandas` and `numpy` to load the `Advertising.csv` dataset, which contains advertising expenditures on TV, radio, and newspapers, along with corresponding sales figures.
    ```python
    import pandas as pd
    import numpy as np

    df = pd.read_csv('[https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/Advertising.csv](https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/Advertising.csv)',
                     index_col=0)
    df.head()
    ```
* **Feature and Target Selection:** The independent variables (`X`) are selected as 'TV', 'radio', and 'newspaper' advertising costs. The dependent variable (`y`) is 'sales', which is the value the model will try to predict.
    ```python
    X = df[['TV', 'radio' , 'newspaper']]
    y = df['sales']
    ```

## 2. Model Definition and Feedforward Process

A linear model is conceptually defined, and its initial prediction is calculated.

* **Model Formula:** The model is based on the linear equation $Y_h = w_0 + w_1X_1 + w_2X_2 + w_3X_3$.
    * $Y_h$: The **predicted output** (predicted sales).
    * $w_0$: The **bias** or **intercept**, representing the base sales when all advertising costs are zero.
    * $w_1, w_2, w_3$: The **weights** or **coefficients**, representing the influence of each feature (`X1`=TV, `X2`=radio, `X3`=newspaper) on the sales.
* **Initial Weight Assignment:** In this manual example, the weights and bias are arbitrarily initialized to `1`. In a real machine learning scenario, these would typically be initialized randomly and then optimized through a training process.
    ```python
    w0 = 1
    w1 = 1
    w2 = 1
    w3 = 1
    ```
* **Feedforward Process:** This is the process of passing the input features through the model with the current weights to get an initial prediction, `Yh`. The code performs a vector operation, calculating a predicted sales value for every row in the DataFrame at once.
    ```python
    Yh = w0 + w1*X.TV + w2*X.radio + w3*X.newspaper
    print(Yh) # Output: A pandas Series containing the initial predicted sales for each row.
    ```
* **Use Cases:** This specific feedforward process is the core calculation for single-layer perceptrons in neural networks and linear regression models. It is the first step before evaluating model performance.

## 3. Error Calculation (Loss Function)

The **error** or **loss** is a metric that quantifies the difference between the model's predictions and the actual values. It tells us how well the model is performing with its current weights.

* **Mean Squared Error (MSE):** The script uses the Mean Squared Error (MSE) as its loss function.
    **Definition:** MSE is calculated as the average of the squared differences between the actual sales (`y`) and the predicted sales (`Yh`). This penalizes larger errors more heavily.
    $$ MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - Y_{h_i})^2 $$
    ```python
    error = ((y - Yh)**2).mean()
    print(error) # Output: A single numerical value representing the total error.
    ```
* **Use Cases:** The MSE is a standard metric for evaluating the performance of regression models. It is also the function that would be minimized during the model training process.

## 4. Next Steps for Model Training (Unimplemented)

The comments in the script outline the next logical steps that would be part of a complete model training process. These steps are crucial for optimizing the model's weights to minimize the error.

* **Calculate Gradient:** The gradient measures the rate of change of the error with respect to each weight ($w_0, w_1, w_2, w_3$).
* **Tune the Value of Weights using Gradients:** An optimization algorithm like **Gradient Descent** would use these gradients and a learning rate to iteratively update the weights. This process is called **backpropagation**, where the error is "backpropagated" through the model to adjust the weights.
* **Calculate Yh and error to check if it reduced or not:** The updated weights would then be used in another feedforward pass, and the new error would be calculated. This entire process would be repeated over many **epochs** until the error is minimized.

## 5. Benefits and Limitations

* **Benefits:** The primary benefit of this script is its educational value. It provides a clear, step-by-step demonstration of the core calculations involved in a linear model's feedforward pass and error evaluation, which is the starting point for understanding more complex neural networks.
* **Limitations:** This script is an incomplete model training pipeline. It only shows the initial feedforward and error calculation and does not include the essential backpropagation and weight update steps. Therefore, it cannot actually "learn" from the data and remains a static model with its initial, arbitrary weights. This approach is not practical for building a real-world predictive model.
