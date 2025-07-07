# Naive Bayes Classifier Explained

## 1. What is Naive Bayes?

Naive Bayes is a family of probabilistic machine learning algorithms based on applying Bayes’ Theorem with the “naive” assumption of conditional independence between every pair of features given the class label.

It is most commonly used in classification problems where the goal is to assign a label (category) to an input vector.

---

## 2. Bayes’ Theorem

Bayes’ Theorem describes the probability of a class given some observed features:

\[
P(Y|X) = \frac{P(X|Y) P(Y)}{P(X)}
\]

Where:
- \( P(Y|X) \): Posterior probability (probability of class \( Y \) given features \( X \))
- \( P(X|Y) \): Likelihood (probability of features \( X \) given class \( Y \))
- \( P(Y) \): Prior probability of class \( Y \)
- \( P(X) \): Prior probability of features \( X \) (often ignored in classification as it’s the same for all classes)

### Naive Assumption

The “naive” part means we assume that all features in \( X \) are independent given \( Y \):

\[
P(X|Y) = P(x_1|Y) \cdot P(x_2|Y) \cdot ... \cdot P(x_n|Y)
\]

---

## 3. Types of Naive Bayes

- **Gaussian Naive Bayes**: Assumes features are continuous and normally distributed (Gaussian).
- **Multinomial Naive Bayes**: For discrete features, commonly used in document classification.
- **Bernoulli Naive Bayes**: For binary/boolean features.

---

## 4. How Naive Bayes Works — Step by Step

Let’s walk through a simple example: Spam Email Classification.

### Step 1: Prepare the Data

Suppose you have a dataset like:

| Email Text         | Is Spam? |
|--------------------|----------|
| Win money now      | Yes      |
| Meeting at 10am    | No       |
| Free offer inside  | Yes      |
| See you tomorrow   | No       |

You extract features: Does the email contain “win”, “free”, “offer”, etc.

### Step 2: Calculate Priors

- \( P(\text{Spam}) = \frac{\text{Number of Spam emails}}{\text{Total emails}} \)
- \( P(\text{Not Spam}) = 1 - P(\text{Spam}) \)

### Step 3: Calculate Likelihoods

For each feature and class, calculate:

- \( P(\text{feature}|\text{Spam}) \)
- \( P(\text{feature}|\text{Not Spam}) \)

This can be done by counting the frequency of the feature in spam and non-spam emails.

### Step 4: Classify New Emails

Given a new email ("Win a free gift"):

- For each class (Spam, Not Spam), calculate the posterior probability:

\[
P(\text{Spam}|\text{features}) \propto P(\text{Spam}) \times P(\text{win}|\text{Spam}) \times P(\text{free}|\text{Spam}) \times P(\text{gift}|\text{Spam})
\]

Choose the class with the higher probability.

---

## 5. Example: Python Implementation (Gaussian Naive Bayes)

Below is a basic workflow using the popular scikit-learn library for a binary classification task (e.g., diabetes risk):

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report

# 1. Load data
df = pd.read_csv('diabetes_data.csv')
X = df.drop(columns=['DiabetesRisk'])
y = df['DiabetesRisk']

# 2. Split data
xtrain, xtest, ytrain, ytest = train_test_split(X, y, train_size=0.75)

# 3. Feature scaling (important for GaussianNB)
scaler = MinMaxScaler()
xtrain_scaled = scaler.fit_transform(xtrain)
xtest_scaled = scaler.transform(xtest)

# 4. Train Naive Bayes
model = GaussianNB()
model.fit(xtrain_scaled, ytrain)

# 5. Evaluate
print("Train Accuracy:", model.score(xtrain_scaled, ytrain))
print("Test Accuracy:", model.score(xtest_scaled, ytest))

# 6. Classification report
print(classification_report(ytest, model.predict(xtest_scaled)))
```

---

## 6. Key Points

- **Assumptions**: Naive Bayes assumes feature independence — often not true, but the method still works surprisingly well in practice.
- **Speed**: Very fast to train and predict.
- **Interpretability**: Probabilistic outputs are easy to interpret.
- **Limitations**: If feature independence is grossly violated, performance may degrade.
- **Zero probabilities**: Use Laplace smoothing to avoid zero probabilities when a feature/class combination doesn't occur in your training data.

---

## 7. More Examples

### Example 1: Text Classification (Multinomial Naive Bayes)

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = ["I love apples", "Buy cheap viagra now", "Meeting at noon", "Free offer just for you"]
labels = [0, 1, 0, 1]  # 0: not spam, 1: spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

new_text = ["Free apples for you"]
X_new = vectorizer.transform(new_text)
print(model.predict(X_new))  # Output: [1] (spam)
```

### Example 2: Bernoulli Naive Bayes

Suitable for binary features (present/absent):

```python
from sklearn.naive_bayes import BernoulliNB
import numpy as np

X = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 1], [0, 0, 0]])
y = [1, 0, 1, 0]  # 1: positive, 0: negative

model = BernoulliNB()
model.fit(X, y)
print(model.predict([[1, 0, 0]]))  # Output: [1]
```

---

## 8. When to Use Naive Bayes

- Text classification (spam, sentiment, topic classification)
- Real-time prediction (fast inference)
- When features are (reasonably) independent

---

## 9. References

- [scikit-learn documentation: Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)
- [Wikipedia: Naive Bayes Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
