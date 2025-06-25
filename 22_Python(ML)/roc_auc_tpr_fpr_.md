# ROC-AUC, TPR-FPR, and Threshold Tuning in Logistic Regression (with Imbalanced Data)

## 1. What is an ROC Curve?

**ROC (Receiver Operating Characteristic) Curve** is a graphical representation of a classifier’s performance across all possible classification thresholds.

- **X-axis:** FPR (False Positive Rate)
- **Y-axis:** TPR (True Positive Rate, a.k.a. Recall/Sensitivity)
- **Purpose:** Visualizes the trade-off between detecting true positives and mistakenly labeling negatives as positives as the decision threshold is varied.

---

## 2. TPR (True Positive Rate) and FPR (False Positive Rate)

- **TPR (Recall/Sensitivity):**
  - Formula: `TPR = TP / (TP + FN)`
  - Meaning: Out of all actual positives, how many did the model correctly identify?

- **FPR:**
  - Formula: `FPR = FP / (FP + TN)`
  - Meaning: Out of all actual negatives, how many did the model incorrectly label as positive?

#### Example Confusion Matrix

|                  | Predicted Positive | Predicted Negative |
|------------------|-------------------|-------------------|
| **Actual Positive** | TP = 80            | FN = 20           |
| **Actual Negative** | FP = 10            | TN = 90           |

- **TPR = 80 / (80 + 20) = 0.80**
- **FPR = 10 / (10 + 90) = 0.10**

---

## 3. AUC (Area Under the ROC Curve)

- **AUC** is the area under the ROC curve, ranging from 0 to 1.
  - **AUC = 1.0**: Perfect classifier
  - **AUC = 0.5**: Random guessing
- **Interpretation:** Probability that the classifier ranks a randomly chosen positive instance higher than a randomly chosen negative one.

---

## 4. Example: Logistic Regression and Threshold Tuning

### Logistic Regression Output

- Produces a probability score for each instance.
- **Default threshold:** 0.5 (probability > 0.5 = positive)
- **Threshold Tuning:** Vary this threshold to get different TPR/FPR values.

### Why Threshold Tuning Matters (Especially for Imbalanced Data)

- **Imbalanced data:** e.g., 95% negatives, 5% positives.
- Default threshold (0.5) may miss most positives (low recall).
- Lowering the threshold increases TPR (more positives detected) but also increases FPR (more negatives misclassified).

---

## 5. Python Example: ROC, AUC, and Thresholds

```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# y_true: true labels, y_pred_proba: predicted probabilities from the model
fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)

plt.plot(fpr, tpr, label='ROC curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

print("AUC:", roc_auc_score(y_true, y_pred_proba))

# Threshold tuning: Find the threshold for TPR >= 0.9
desired_tpr = 0.9
idx = next(i for i, x in enumerate(tpr) if x > desired_tpr)
best_threshold = thresholds[idx]
print(f"Threshold for TPR >= 0.9: {best_threshold:.2f}")
```

---

## 6. Threshold Tuning Using TPR-FPR (for Biased Data)

- **Objective:** Maximize positive detection (recall) while keeping false alarms (FPR) within acceptable limits.
- **Approach:** Use the ROC curve to select a threshold that balances TPR and FPR according to business needs.

### Example Threshold Table

| Threshold | TPR  | FPR  | Comment                        |
|-----------|------|------|-------------------------------|
| 0.5       | 0.60 | 0.05 | Default, misses positives     |
| 0.3       | 0.80 | 0.15 | More positives, more mistakes |
| 0.2       | 0.90 | 0.30 | High recall, high FPR         |

- **Lower threshold** → higher TPR, but also higher FPR.
- **Choose threshold** based on which type of error (missed positives vs. false alarms) is more costly for your application.

---

## 7. Summary

- **ROC curve:** Visualizes the trade-off between TPR (recall) and FPR as threshold changes.
- **AUC:** Summarizes classifier’s performance (higher is better).
- **Threshold tuning:** Essential for imbalanced data—lowering the threshold improves recall but increases false positives.
- **Best threshold:** Depends on business context—select using ROC curves, TPR/FPR trade-offs, or maximizing F1-score.

---

**Want to see more code or a real dataset example? Let me know!**
