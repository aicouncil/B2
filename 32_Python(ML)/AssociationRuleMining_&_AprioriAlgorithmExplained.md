# Association Rule Mining & Apriori Algorithm Explained

## What is Association Rule Mining?

Association Rule Mining is a **rule-based machine learning** technique that discovers interesting relationships between variables in large databases. It's primarily used for **market basket analysis** - understanding which products are frequently bought together.

### Key Components:
1. **Itemset**: A collection of items (e.g., {Milk, Bread})
2. **Rule**: An implication of form X → Y (e.g., {Diapers} → {Beer})

## The Apriori Algorithm

Apriori is the **most classic algorithm** for association rule mining. It works on the principle that:
> "All non-empty subsets of a frequent itemset must also be frequent"

### How It Works (Step-by-Step):

1. **Identify Frequent Itemsets**:
   - Scan database to find itemsets with ≥ minimum support
   - Prune infrequent itemsets

2. **Generate Association Rules**:
   - From frequent itemsets, generate rules with ≥ minimum confidence
   - Prune weak rules

### Key Metrics:

| Metric       | Formula                          | What It Measures                     | Example Interpretation               |
|--------------|----------------------------------|--------------------------------------|--------------------------------------|
| **Support**  | P(X ∩ Y)                        | How frequently itemset appears       | 30% of transactions contain milk     |
| **Confidence**| P(Y\|X) = Support(X∪Y)/Support(X)| How often Y appears with X           | 70% of milk buyers also buy bread    |
| **Lift**     | P(Y\|X)/P(Y)                    | Strength of association              | Lift=2 means X makes Y twice as likely|

## Real-World Example: Grocery Store

**Sample Transactions**:
1. {Milk, Bread, Eggs}
2. {Milk, Bread, Diapers, Beer}
3. {Bread, Eggs, Beer}
4. {Milk, Eggs, Beer}
5. {Bread, Diapers, Beer}

### Step 1: Find Frequent Itemsets (min_support=40%)

| Itemset          | Support |
|------------------|---------|
| {Milk}           | 60%     |
| {Bread}          | 80%     |
| {Eggs}           | 60%     |
| {Beer}           | 80%     |
| {Milk, Bread}    | 40%     |
| {Bread, Beer}    | 60%     |

### Step 2: Generate Rules (min_confidence=50%)

1. **Milk → Bread**  
   - Support: 40%  
   - Confidence: 40%/60% = 66.7%  
   - Lift: 66.7%/80% = 0.83 (not useful)

2. **Bread → Beer**  
   - Support: 60%  
   - Confidence: 60%/80% = 75%  
   - Lift: 75%/80% = 0.94 (not useful)

3. **Diapers → Beer**  
   - Support: 40%  
   - Confidence: 100%  
   - Lift: 100%/80% = 1.25 (positive correlation)

## Practical Applications

1. **Retail**: Product placement & bundling
2. **Healthcare**: Finding symptom-disease relationships  
3. **Web Usage**: Recommending related pages/content
4. **Fraud Detection**: Identifying suspicious pattern combinations

## Advantages vs. Limitations

**Pros**:
- Easy to understand and implement
- Works well with categorical data
- Generates interpretable rules

**Cons**:
- Computationally expensive for large datasets
- May generate many trivial rules
- Requires careful tuning of support/confidence thresholds

## Python Implementation Example

```python
from mlxtend.frequent_patterns import apriori, association_rules

# Generate frequent itemsets
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)

# Generate rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Filter and sort
rules[(rules['lift'] > 1.2) & (rules['confidence'] > 0.7)].sort_values('confidence', ascending=False)

# This would output rules like:
        antecedents    consequents  support  confidence  lift
0       {Diapers}       {Beer}       0.4     1.0       1.25
1       {Milk, Bread}   {Eggs}       0.2     0.75      1.15
