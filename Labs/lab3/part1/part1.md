Explain the concepts and Gaussian NB algorithm to the lab assistant:

“Gaussian Naïve Bayes is a classification algorithm based on Bayes’ theorem. It calculates the probability of a class given the features. The ‘naïve’ part is assuming all features are independent, and the ‘Gaussian’ part is assuming each feature follows a normal distribution.

During training, the model computes the prior probability for each class and the mean and standard deviation for every feature in each class.

When predicting a new sample, it uses the Gaussian formula to compute the likelihood of each feature for each class, multiplies these probabilities together, multiplies by the class prior, and chooses the class with the highest posterior probability (MAP).

Pros:

- It’s very fast, simple, interpretable, and works well on high-dimensional data.”

Cons:

- Dosent perform well with more complex datasets
