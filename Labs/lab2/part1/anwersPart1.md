THE ANSWERS FOR THE FIRST PART

1. **When can you use linear regression?**
   You can use linear regression when you think the relationship between your input (x) and output (y) is roughly a straight line — or at least can be made linear after transforming the data.
   It’s good for problems where:
   -- The change in y is proportional to the change in x.
   -- You want a model that is simple, fast, and easy to interpret.

2. **How can you generalize linear regression models to account for more complex relationships among the data?**
   BASIS FUNCTIONS! We transform the input data (Ex. polynomial or gaussian) so a linear model can fit nonlinear realationships between variables

3. **What are the basis functions?**
   In the paper: Polynomial and gaussian
   Basis functions are transformations of the input data that help the model fit more complicated patterns.
   For example:
   -- Polynomial functions (x, x², x³, …)
   -- Gaussian functions (bell-shaped curves)
   They let the model build a curve using a combination of these simpler functions.

4. **How many basis functions can you use in the same regression model?**
   A: In principle we can use as many bases as we want. But more bases increase flexibility and risk overfitting. Too few -> the model is too simple and will underfit. Too many -> the model is to "wiggly" and fits to noise instead of trends of the data.

   (In the paper we saw that they got wild oscillations with 30 Gaussians).

5. **Can overfitting be a problem? And if so, what can you do about it?**
   A: Yes, overfitting can happen when the model tries to follow the noise in the data instead of the real pattern.
   To prevent it, you can:
   -- Use regularization (like Ridge or Lasso regression) to limit how big the model’s coefficients can get.
   -- Use cross-validation to check if your model works well on unseen data.
   -- Avoid using too many basis functions or overly complex models.
