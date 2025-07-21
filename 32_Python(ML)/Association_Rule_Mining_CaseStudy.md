# Detailed Summary of Association Rule Mining Notebooks

## Overview
This analysis covers two Jupyter notebooks demonstrating association rule mining using the Apriori algorithm. The first notebook (`B12_Associantion_rule_mining.ipynb`) uses a small synthetic dataset, while the second (`b12-association-rules-recommendar-ipynb.ipynb`) analyzes real-world retail data from the UCI Online Retail II dataset.

---

## Notebook 1: B12_Associantion_rule_mining.ipynb

### Key Components

1. **Dataset Preparation**
   - Small transactional dataset with grocery items:
     ```python
     dataset = [['Milk','Onion','Nutmeg','Kidney Beans','Eggs','Yogurt'],
                ['Dill','Onion','Nutmeg','Kidney Beans','Eggs','Yogurt'],
                ['Milk','Apple','Kidney Beans','Eggs'],
                ['Milk','Unicorn','Corn','Kidney Beans','Yogurt'],
                ['Corn','Onion','Onion','Kidney Beans','Ice cream','Eggs']]
     ```

2. **Data Transformation**
   - Uses `TransactionEncoder` from `mlxtend` to convert categorical data into a boolean matrix:
     ```python
     te = TransactionEncoder()
     te.fit(dataset)
     df = pd.DataFrame(te.transform(dataset), columns=te.columns_)
     ```
   - Output: Boolean DataFrame where `True` indicates item presence.

3. **Frequent Itemset Mining**
   - Applies Apriori algorithm with `min_support=0.5`:
     ```python
     frequent_items = apriori(df, use_colnames=True, min_support=0.5)
     ```
   - Results show itemsets like `(Kidney Beans)` (support=1.0) and `(Eggs)` (support=0.8).

4. **Association Rule Generation**
   - Rules derived with `confidence` metric (threshold=0.6):
     ```python
     rules = association_rules(frequent_items, metric='confidence', min_threshold=0.6)
     ```
   - Key metrics:
     - **Lift**: e.g., 1.25 for `(Onion) -> (Eggs)` indicates positive correlation.
     - **Confidence**: 100% for `(Onion) -> (Eggs)` means all onion purchases included eggs.

5. **Rule Filtering**
   - Final output focuses on key columns:
     ```python
     res1 = res[['antecedents','consequents','support','confidence','lift']]
     ```

---

## Notebook 2: b12-association-rules-recommendar-ipynb.ipynb

### Key Components

1. **Data Loading & Cleaning**
   - Loads UCI Online Retail II dataset:
     ```python
     df = pd.read_csv('/kaggle/input/online-retail-ii-uci/online_retail_II.csv')
     ```
   - Preprocessing steps:
     - Drops NA values (`df1 = df.dropna()`).
     - Filters positive quantities (`df2 = df1[~(df1['Quantity'] < 1)]`).
     - Removes duplicates (`df3 = df2.drop_duplicates()`).
     - Standardizes text (lowercase + strip whitespace).

2. **Data Structuring**
   - Creates a basket matrix (customer-item matrix):
     ```python
     df_basket = df3.groupby(['Customer ID','Description'])['Quantity'].sum().unstack().fillna(0)
     df_basket = df_basket.apply(lambda x: x > 0)
     ```

3. **Frequent Itemset Mining**
   - Runs Apriori with `min_support=0.06`:
     ```python
     frequent_items = apriori(df_basket, use_colnames=True, min_support=0.06)
     ```

4. **Association Rule Generation**
   - Generates rules with `lift` metric (threshold=1):
     ```python
     rules = association_rules(frequent_items, metric='lift', min_threshold=1)
     ```
   - Example rule: `['green regency teacup and saucer'] -> ['roses regency teacup and saucer']` with high lift.

5. **UK-Specific Analysis**
   - Filters data for UK customers:
     ```python
     df_uk = df[df['Country'] == 'United Kingdom']
     ```
   - Repeats preprocessing and rule mining for invoice-based recommendations.

6. **Recommendation System**
   - Saves rules to CSV for lookup:
     ```python
     r2.to_csv('invoice_recommendar.csv')
     ```
   - Example query:
     ```python
     item_selected = "['6 ribbons rustic charm']"
     dfi_recommendar[dfi_recommendar['antecedents'] == item_selected].consequents
     ```

---

## Key Concepts Demonstrated

### 1. **Apriori Algorithm**
   - **Purpose**: Identifies frequent itemsets by pruning candidates below `min_support`.
   - **Example**: In Notebook 1, `(Kidney Beans, Eggs)` has support=0.8 (appears in 4/5 transactions).

### 2. **Association Metrics**
   - **Support**: Frequency of itemset (e.g., `(Milk)` has support=0.6 in Notebook 1).
   - **Confidence**: Probability of consequent given antecedent (e.g., 100% for `(Onion) -> (Eggs)`).
   - **Lift**: Measures dependency (lift > 1 implies positive correlation).

### 3. **Practical Applications**
   - **Market Basket Analysis**: Identifies product pairs like `(Kidney Beans, Eggs)`.
   - **Recommendation Systems**: Generates suggestions (e.g., customers buying teacups might like roses-patterned variants).

---

## Comparative Analysis

| **Aspect**               | **Notebook 1**                          | **Notebook 2**                          |
|--------------------------|----------------------------------------|----------------------------------------|
| **Dataset**              | Synthetic (5 transactions)             | Real-world (Online Retail II)          |
| **Preprocessing**        | Simple boolean encoding                | Extensive cleaning (NA, duplicates)    |
| **Rule Focus**           | Basic grocery items                    | Retail product recommendations        |
| **Use Case**             | Educational demonstration              | Practical recommendation system       |

---

## Code Snippets for Key Operations

### 1. Data Encoding (Notebook 1)
```python
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

## 2. Rule Generation (Notebook 2)
```python
from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_items, metric='lift', min_threshold=1)
rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

## 3. Recommendation Query
```python
item_selected = "['green regency teacup and saucer']"
recommendations = df_recommend[df_recommend['antecedents'] == item_selected].consequents

## Lessons Learned

1. **Data Quality Matters**: Notebook 2 highlights the importance of cleaning (handling NA values, duplicates).
2. **Metric Selection**: Confidence vs. lift depends on use cases (predictive accuracy vs. dependency strength). 
3. **Scalability**: Apriori works well for small datasets but may need optimizations (e.g., FP-Growth) for larger ones.
