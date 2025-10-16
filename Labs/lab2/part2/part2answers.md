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
   KNN makes no assumptions about the shape of the decision boundary, it is non-parametric. It can therefore model non-linear relationships simply by relying on local neighborhood similarity.

4. **Is KNN sensible to the number of features in the dataset?**
   A: Short answer YES.
   KNN suffers from the "curse of dimensionality", which means: as the number of features grows, distances between points become less meaningful, requiring exponentially more data and leading to overfitting.
   To mitigate this:
   -- Use feature selection or dimensionality reduction (PCA)
   -- Normalize features to comparable scales

5. **Can you use KNN for a regression problem?**
   A: Short answer YES.
   Although often used for classification, KNN can perform regression by averaging (or weighting) the target values of the k nearest neighbors instead of voting on classes.

6. **What are the Pros and Cons of KNN?**
   PROS:

   - simple and intuitive algorithm
   - No training phase. Fast to set up (lazy learning)
   - Works for non-linear data distributions
   - Can handle both classification and regression tasks

   CONS:

   - Prediction phase is slow and memoryintensive (must compare to all training points)
   - Requires scaling/normalization of features (espacially with Euclidean distance
   - Not suitable for high-dimensional data (curse of dimensionality)
   - Sensitive to irrelevant or noisy features
