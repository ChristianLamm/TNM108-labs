1. **Why choosing a good value for k is important in KNN?**
   A: Because k controls how many neighbors are considered when classifying a new data point, it directly affects model bias and viarance.
   -- a SMALL k makes the model sensitive to noise (low bias, high variance -> overfitting)
   -- a LARGE k oversmooths the decision boundary (high bias, low variance -> underfitting)
   Thus, the choice of k strongly influences both accuracy and robustness of the classifier.

2. **How can you decide a good value for k?**
   A: there is no universal best k, it depends on the dataset.
   Some typical approaches:
   -- Empirical testing: try several k values and compare performance
   -- Elbow method: plot accuracy versus k and choose the point where improvement levels off
   -- Use odd k when the number of classes is even to avoid ties

3. **Can you use KNN to classify non-linearly separable data?**
   A: Short answer YES.
   KNN doesn’t assume that data is straight-line separable. It simply looks at the nearby data points, so it can handle curved or complex boundaries very well.

4. **Is KNN sensible to the number of features in the dataset?**
   A: Short answer YES.
   If there are too many features (columns), KNN can struggle — this is called the curse of dimensionality.
   When that happens, distances between points become less meaningful, and you might need much more data.
   To fix this, you can:
   -- Use fewer features, or
   -- Reduce dimensions using PCA, and
   -- Normalize the data so all features are on the same scale.

5. **Can you use KNN for a regression problem?**
   A: Short answer YES.
   It is often used for classification, but KNN can perform regression. In regression, it takes the average (or weighted average) of the values from the k nearest neighbors to make a prediction.

6. **What are the Pros and Cons of KNN?**
   PROS:

   - simple and intuitive algorithm
   - No training phase. Fast to set up (lazy learning)
   - Works for non-linear data distributions
   - Can handle both classification and regression tasks

   CONS:

   - Prediction phase is slow and memoryintensive (must compare to all training points)
   - Requires scaling/normalization of features (espacially with Euclidean distance)
   - Needs a lot of memory to store all data.
   - Doesn’t work well with too many features or noisy data (cures of dimensionality)
