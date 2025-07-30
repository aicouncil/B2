The provided meeting notes from July 26, 2025, detail the AI Council's end-to-end project to build a predictive model for property prices using real estate data.

Key aspects of the project and discussion points include:

  * **Data Pre-processing:**
    
      * Initial steps involved checking data types, unique values, and handling a significant number of null values in the 'society' column, which was eventually dropped due to its uninformative nature.
      * Bias in the 'area type' column was addressed by combining 'buildup area', 'plot area', and 'carpet area' into an 'others' category.
      * The 'availability' column was transformed into "Ready To Move" and "Under Construction" categories.
      * The 'location' column was standardized, and locations with fewer than 30 samples were filtered out, reducing the number of unique locations to 100.
      * The 'size' column was processed to extract only the numerical part representing the number of rooms, and unrealistic values (e.g., 10 or 12 bedrooms) were capped at six.
      * The 'total square feet' column, containing non-numerical values like ranges, was normalized by converting numerical values to float and calculating the average for ranges.
      * Missing values in 'total square feet' were imputed using the 'size' column, and missing 'size' values were imputed based on 'total square feet'.
      * Missing 'bath' values were filled by adding one to the corresponding 'size' (bedroom count).
      * Missing 'balcony' values were imputed based on the 'size' column (one balcony for two or fewer bedrooms, two otherwise).

  * **Outlier Detection and Handling:**
    
      * Outliers were identified in 'total square feet' and 'price' columns.
      * A "price per square foot" (PPS) column was calculated to aid outlier analysis.
      * A per-location outlier handling strategy was adopted, involving quantile-based clipping within each location group for 'total square feet' and 'price per square foot'.

  * **Model Training and Interpretation:**
    
      * Categorical features were converted using one-hot encoding.
      * The data was split into training and testing sets.
      * A linear regression model was trained, and its performance was evaluated using mean absolute error and R2 score.
      * Rehan Ahmed Siddique and Raksh Pal suggested data scaling for better model interpretation, as coefficients were problematic due to varying feature magnitudes. The AI Council confirmed scaling as crucial for accurate interpretation.

  * **Model Deployment Preparation:**
    
      * The trained linear regression model ('model A') and the MinMax scaler object were saved as artifacts using the `joblib` library for future deployment.

**Suggested next steps:**

  * The group will finish the current work up to the deployment.
  * The group will create the user interface and use a cloud service to deploy the model.
