THE ANSWERS FOR THE FIRST PART

1. When can you use linear regression?
   When there is a linear realation between variables, and the data is roughly continuous, independent, and evenly distributed (no big outliers or curved trends).

2. How can you generalize linear regression models to account for more complex relationships among the data?
   BASIS FUNCTIONS! We transform the input data (Ex. polynomial or gaussian) so a linear model can fit nonlinear realationships between variables

3. What are the basis functions?
   In the paper: Polynomial and gaussian

4. How many basis functions can you use in the same regression model?
   A: In principle we can use as many bases as we want. But more bases increase flexibility and risk overfitting. Too few -> themodel is too simple and will underfit. Too many -> the model is to "wiggly" and fits to noise instead of trends of the data.

   (In the paper we saw that they got wild oscillations with 30 Gaussians).

5. Can overfitting be a problem? And if so, what can you do about it?
   A: Yes it can, it can wrongly represent the data, -> the output can get very extreme values between data points.
   l A: In principle we can use as many bases as we want. But more bases increase flexibility and risk overfitting. Too few -> th
   (In the paper we saw that they got wild oscillations with 30 Gaussians).
