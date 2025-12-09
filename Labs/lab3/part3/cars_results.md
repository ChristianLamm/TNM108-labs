## Car Evaluation Quality – Console Run (18 Nov 2025)

**Setup.** Using the existing `part3/cars.py` script, every column in `data_cars.csv` is cast to the `category` dtype, encoded via `.cat.codes`, shuffled once with `np.random.permutation`, and evaluated with 10-fold cross-validation. The script prints three per-class tables (F1, precision, recall) for the six configured classifiers: linear SVM, Multinomial Naive Bayes, logistic regression, k-NN, decision tree, and random forest. No extra models were added for this run—only the console output was inspected.

### Per-class F1 scores (from console)

| Model                        | acc    | good   | unacc  | vgood  |
| ---------------------------- | ------ | ------ | ------ | ------ |
| Linear SVM                   | 0.2706 | 0.0000 | 0.8471 | 0.0000 |
| Naive Bayes                  | 0.0404 | 0.0000 | 0.8253 | 0.0000 |
| Logistic Regression          | 0.2397 | 0.0000 | 0.8212 | 0.2617 |
| k-NN (k=5, distance weights) | 0.8111 | 0.5545 | 0.9579 | 0.7379 |
| Decision Tree                | 0.9651 | 0.9118 | 0.9930 | 0.9697 |
| Random Forest                | 0.9633 | 0.9353 | 0.9934 | 0.9771 |

The same ordering appears in the precision/recall tables: linear SVM, Naive Bayes, and logistic regression struggle on the minority `good`/`vgood` classes (precision and recall collapse to 0). k-NN improves recall for `vgood`, but the tree-based models dominate across all categories with >0.9 precision and recall simultaneously.

### Answer to the lab question

Yes—there **are** machine-learning algorithms that perform substantially better on `data_cars.csv` than the original linear SVM/Naive Bayes/logistic/k-NN baselines. The console output shows that:

1. **Decision trees** capture the rule-like structure of the categorical features, reaching F1 scores above 0.91 for every class (up to 0.99 for `unacc`), far beyond the linear models.
2. **Random forests** provide similar but even more stable results (per-class F1 up to 0.98 for `vgood`), indicating ensemble trees consistently deliver near-perfect predictions.
3. Because our current script does not include alternative SVM kernels, we cannot cite new SVM numbers, but the dramatic jump from the tree-based methods already answers the question: non-linear models such as decision trees and random forests clearly outperform the earlier approaches on this dataset.

These findings come directly from the latest console run (see the terminal transcript captured on 18 Nov 2025).
