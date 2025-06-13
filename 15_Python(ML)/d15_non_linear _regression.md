## Explanation of Non-Linear Regression Section

### 1. **Applying 2-Degree Non-Linear Transformation on Advertising Data (TV, radio)**

- **What does this mean?**
  - We take the original features, `TV` and `radio`, and expand them to include non-linear terms:
    - `TV`
    - `radio`
    - `TV^2` (square of TV)
    - `radio^2` (square of radio)
    - `TV * radio` (interaction term)
  - This transformation allows the model to fit curves (not just straight lines) to the data.

- **Why do this?**
  - Real-world relationships are often not perfectly linear. Adding these terms helps the model capture more complex patterns.

- **Example:**
  ```python
  from sklearn.preprocessing import PolynomialFeatures

  poly = PolynomialFeatures(degree=2, include_bias=False)
  X_poly = poly.fit_transform(advertising[['TV', 'radio']])
  ```

---

### 2. **Building a Predictive Model Using Transformed Data**

- **What happens here?**
  - We use the new polynomial features (`TV`, `radio`, `TV^2`, `radio^2`, `TV*radio`) to train a regression model.
  - The model tries to find the best fit using these expanded features.

- **Example:**
  ```python
  from sklearn.linear_model import LinearRegression

  model_poly = LinearRegression()
  model_poly.fit(X_poly, advertising['sales'])
  ```

---

### 3. **Comparing Non-Linear Model Performance With Linear Model**

- **How do we compare?**
  - We use metrics like Mean Absolute Error (MAE) to measure prediction accuracy.
  - Lower MAE means better performance.

- **Example:**
  ```python
  y_pred_poly = model_poly.predict(X_poly)
  mae_poly = abs(advertising['sales'] - y_pred_poly).mean()
  print(mae_poly)

  # Compare with earlier linear model's MAE
  print(mae_linear)
  ```

- **Table Example:**

  | Model Type              | MAE (lower is better) |
  |-------------------------|----------------------|
  | Linear Model            | 0.8                  |
  | Non-linear Model (Poly) | 0.6                  |

---

### 4. **Visualization and Interpretation**

- **Why visualize?**
  - Plots help us see how well the model predictions match the actual data.

- **Example code:**
  ```python
  plt.scatter(advertising['sales'], y_pred_poly, label="Non-linear predictions")
  plt.plot([min(advertising['sales']), max(advertising['sales'])],
           [min(advertising['sales']), max(advertising['sales'])], 'r--', label="Perfect prediction")
  plt.xlabel("Actual sales")
  plt.ylabel("Predicted sales")
  plt.legend()
  plt.show()
  ```

- **Interpretation:**
  - If the non-linear model's predictions are closer to the actual data (lower MAE, better plot alignment), it is a better fit.
  - But if it overfits (fits noise, not the real pattern), the improvement may not generalize.

---

### 5. **Key Takeaways**

- **Polynomial regression**: Adds non-linear features to linear models.
- **Feature engineering**: Creating new (squared, interaction) features can improve model performance.
- **Model comparison**: Always compare metrics to see if added complexity is worth it.
- **Visualization**: Helps interpret model quality.
