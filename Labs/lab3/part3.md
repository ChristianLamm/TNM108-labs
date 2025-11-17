1. Yes, much better results. We get an much higher Mean (R^2) value, and a dropped MSE results among all tests.
   [Want to have R^2 --> 1, MSE --> 0]
   R^2 measures how much the variance in the target your model explains. If R^2 = 0 it means that the model is no better than predicting the mean.
   MSE (Mean squared error) is the avarage of squared prediction errors. Lower is better, because each prediction is on avarage closed to the true value.

By shuffling once (with a fixed seed for reproducibility) before creating the folds, you ensure each fold is a random, representative mix of the entire dataset. That makes:

Models train on diversified data in each fold.
Validation sets look like the overall distribution, giving a fairer estimate.
The variance of R^2 shrinks and the mean score usually improves because the model isn’t punished by unlucky splits. 2.

2.
