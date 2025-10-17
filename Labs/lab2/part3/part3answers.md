1. What is the basic idea/intuition of SVM?
   A: SVMs are maximum margin classifiers. you want to find the lin, or plane that best seperates the classes in the dataset while maximizing the margin. The distance between the dividing line and the nearest data points from each class. Points further away do not affect the model.

2. What can you do if the dataset is not linearly separable?
   A: SVMs can use a kernel transformation to project the data into a higher-dimensional space where it becomes linearly separable. The kernel trick computes inner products in the higher-dimensional space without explicitly transforming the data.

3. Explain the concept of Soften Margins
   A: a perfect separation may not be possible so SVM allow soft margins. THis means some points can be included even if they violate the margin/be missclassified if it means they improve the model. the softness depends on parameter C, tuned by cross-validation.
   Large C → Hard margin (few misclassifications allowed).

   Small C → Soft margin (more tolerance for errors).

4. What are the pros and cons of SVM?
   A:
   Pros:
   memmory efficieint (few support vectors),
   Fast point rediction
   Works well with high-dimensional data
   Versatille due to kernel methods
   cons:
   difficult parameter tuning
   Parameter not easily interpreted(e.g C)
   Can be slow to train on large datasets
