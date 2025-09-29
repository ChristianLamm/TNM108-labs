**PISSASS**

1. What are the relevant features of the Titanic dataset. Why are they relevant?
   Most of the features are relevant in some way. But ticket number and embarked might be useless information. For example is age, sex and pclass some of the more important information since priotitation.

2. Can you find a parameter configuration to get a validation score greater than 62% ?
   "Drop, Scale och sånt" - Lambo
   We can drop irrelevant features like ticket (number), Embarked, Cabin, usea MinMaxScaler for matching all values in our dataset and categorical variables like sex with LabelEncoder we can bump up our validation score. We can also choose different cluster algorithm, and max iterations.

3. What are the advantages/disadvantages of K-Means clustering?
   Pros:

   - Simple and fast to implement. Straightforward mathematical operations. (Distance calcs, averaging)
   - Scales well to large datasets. Time complexity is linear with respect to data points.
   - Works well when clusters are spherical and similar in size.
   - Easy to interpret results. The output is intuitive, each data point is assigned to a cluster, which is represented by its centroid. Simple to visualize

   Cons:

   - Can get different outcomes depending on which data point you choose as a starting cluster centroid,
   - and also the ordering of the data can change the outcome.
   - You also have to pre-specify the number of clusters.
   - It is sensitive to outliers.
   - can require a large amount of data

4. How can you address the weaknesses?

   One big weakness of K-means is the random initialization problem. We can always try to make it as good as possible with incresing 'n_init' to try multiple random starts, or use k-means++ initialization for smarted centeriod placement.
   For handling outliers we can try to identify and remove them in a preprocessing stage, or use other scalermethods like RobustScaler (uses median and interquartile) instead of MinMaxScaler (Sensitive to outliers because it uses min & max values), or consider another algorithms like k-mediods which use medians instead of mean
