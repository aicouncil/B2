# Data Preprocessing and Encoding: Detailed Explanation and Examples

## 1. Convert Non-Numerical Values into Numerical Forms

### Why?
Most machine learning algorithms require numerical input. Therefore, categorical (non-numerical) variables must be converted into numbers.

---

### Example: Checking Unique Values in Categorical Columns

```python
print(X['Item_Identifier'].unique())
print(X['Item_Fat_Content'].unique())
print(X['Item_Type'].unique())
print(X['Outlet_Size'].unique())
print(X['Outlet_Location_Type'].unique())
print(X['Outlet_Type'].unique())
```

**Output Example:**
```
['FD' 'DR' 'NC']
['low fat' 'regular']
['Dairy' 'Soft Drinks' 'Meat' ... 'Seafood']
['Medium' 'High' 'Small']
['Tier 1' 'Tier 3' 'Tier 2']
['Supermarket Type1' 'Supermarket Type2' 'Grocery Store' 'Supermarket Type3']
```

**Explanation:**  
- Each `print()` statement shows all the unique categories in a column.
- This helps you understand what values need to be encoded as numbers.
- For example, 'Item_Fat_Content' has values like 'low fat' and 'regular', which need to be numerically represented.

---

## 2. Encoding Ordinal Data

### What is Ordinal Data?
Ordinal data is categorical data with an order or ranking (e.g., "Small", "Medium", "High").

#### Example DataFrame (first 2 rows):

| Item_Identifier | Item_Weight | Item_Fat_Content | Item_Visibility | Item_Type     | Item_MRP | Outlet_Identifier | Outlet_age | Outlet_Size | Outlet_Location_Type | Outlet_Type         |
|-----------------|-------------|------------------|-----------------|--------------|----------|-------------------|------------|-------------|----------------------|---------------------|
| FD              | 9.3         | low fat          | 0.016047        | Dairy        | 249.8092 | 49                | 26         | Medium      | Tier 1               | Supermarket Type1   |
| DR              | 5.92        | regular          | 0.019278        | Soft Drinks  | 48.2692  | 18                | 16         | Medium      | Tier 3               | Supermarket Type2   |

---

## 3. Label Encoding (for Ordinal Data)

### Why?
Ordinal values have a meaningful order. For example, Outlet_Size: Small < Medium < High.

### How?

```python
Xt['Item_Fat_Content'] = X['Item_Fat_Content'].map({'low fat':0, 'regular':1})
Xt['Outlet_Size'] = X['Outlet_Size'].map({'Small' : 0 , 'Medium' : 1, 'High' : 2})
Xt['Outlet_Location_Type'] = X['Outlet_Location_Type'].map({'Tier 1':1, 'Tier 2' : 2 , 'Tier 3' : 3 })
```

#### Example (after encoding):

| Item_Identifier | ... | Item_Fat_Content | ... | Outlet_Size | Outlet_Location_Type | ... |
|-----------------|-----|------------------|-----|-------------|---------------------|-----|
| FD              | ... | 0                | ... | 1           | 1                   | ... |
| DR              | ... | 1                | ... | 1           | 3                   | ... |

**Explanation:**  
- 'low fat' → 0, 'regular' → 1  
- 'Small' → 0, 'Medium' → 1, 'High' → 2  
- 'Tier 1' → 1, 'Tier 2' → 2, 'Tier 3' → 3  

**When to use?**  
- When categories have a meaningful order (ordinal).

---

## 4. One-Hot Encoding (for Nominal Data)

### Why?
Nominal data has no meaningful order (e.g., 'A', 'B', 'C', 'D'). One-hot encoding creates a new binary column for each category.

### Example:

#### Original Data

```python
dt = pd.DataFrame({'cat' : ['A','B','A','C','B','C','C','A','D']})
```

#### One-hot Encoding

```python
pd.get_dummies(dt, dtype=int)
```

#### Output Table

|    | cat_A | cat_B | cat_C | cat_D |
|----|-------|-------|-------|-------|
| 0  | 1     | 0     | 0     | 0     |
| 1  | 0     | 1     | 0     | 0     |
| 2  | 1     | 0     | 0     | 0     |
| 3  | 0     | 0     | 1     | 0     |
| 4  | 0     | 1     | 0     | 0     |
| 5  | 0     | 0     | 1     | 0     |
| 6  | 0     | 0     | 1     | 0     |
| 7  | 1     | 0     | 0     | 0     |
| 8  | 0     | 0     | 0     | 1     |

**Explanation:**  
- Each original value is represented by a column with 1 (present) or 0 (absent).
- No ordinal relationship is implied.

---

## 5. Applying One-hot Encoding to Main Data

```python
Xts = pd.get_dummies(Xt , dtype=int)
```

#### Output (first few columns):

| Item_Weight | Item_Fat_Content | ... | Item_Identifier_FD | ... | Outlet_Type_Supermarket Type1 | ... |
|-------------|------------------|-----|--------------------|-----|-------------------------------|-----|
| 9.3         | 0                | ... | 1                  | ... | 1                             | ... |
| 5.92        | 1                | ... | 0                  | ... | 0                             | ... |

**Explanation:**  
- All remaining categorical variables (not ordinal) get expanded to multiple columns.
- For example, if 'Item_Identifier' has values 'FD', 'DR', 'NC', you get columns: 'Item_Identifier_FD', 'Item_Identifier_DR', 'Item_Identifier_NC'.

---

## 6. Output Variable `y`

```python
y = df['Item_Outlet_Sales']
```
**Explanation:**  
- This is the target column (the value we want to predict).

---

## 7. Train-Test Split

```python
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(Xts, y, train_size=0.75)
```

**Explanation:**  
- Splits the data into training (75%) and testing (25%) sets.
- Training data is used to fit the model, testing data is for evaluation.

---

## 8. Train the Model

```python
from sklearn.linear_model import LinearRegression

model_A = LinearRegression()
model_A.fit(xtrain, ytrain)
```

**Explanation:**  
- Creates a linear regression model and fits it to the training data.

---

## 9. Evaluate Model Performance

```python
ytrainPred = model_A.predict(xtrain)
ytestPred = model_A.predict(xtest)
maeTrain = abs(ytrain - ytrainPred).mean()
maeTest = abs(ytest - ytestPred).mean()

print("Mean absolute error on training data", maeTrain)
print("Mean absolute error on test data", maeTest)
```

**Explanation:**  
- Predicts sales for both training and testing data.
- Calculates Mean Absolute Error (MAE): average absolute difference between predictions and true values.
- Lower MAE means better performance.

---

## **Summary Table**

| Step                    | What it Does                                                      | Example/Output                   |
|-------------------------|-------------------------------------------------------------------|----------------------------------|
| Unique Values           | Shows all unique categories in each column                        | `['low fat', 'regular']`         |
| Label Encoding          | Converts ordinal categories to numbers                            | 'High' → 2, 'Medium' → 1         |
| One-hot Encoding        | Converts nominal categories to binary columns                     | 'cat_A', 'cat_B', ...            |
| Train/Test Split        | Splits data into train/test sets                                 | xtrain, xtest, ytrain, ytest     |
| Model Training          | Fits a linear regression model                                   | `model_A.fit(xtrain, ytrain)`    |
| Model Evaluation        | Measures how well the model fits and generalizes                 | MAE values                       |

---

## **When to Use Which Encoding?**

- **Label Encoding**: Use for ordinal data.
- **One-hot Encoding**: Use for nominal data.

---

## **Practical Example**

Suppose you have a column 'Color' with values `['Red', 'Green', 'Blue']`.  
- If 'Color' is ordinal (e.g., 'Low', 'Medium', 'High'), use label encoding.
- If 'Color' is nominal, use one-hot encoding: new columns 'Color_Red', 'Color_Green', 'Color_Blue'.

---

If you want code snippets or more examples for any step above, let me know!
