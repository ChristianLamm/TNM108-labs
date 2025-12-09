**To pass Part 2:**
Write a text classification pipeline to classify movie reviews as either positive or negative.
Find a good set of parameters for the pipeline you have created by using grid search.
Show your result to the lab assistant.

---

This script implements a Supervised Machine Learning pipeline for Sentiment Analysis (classifying text as "positive" or "negative").

Here is a breakdown of the techniques and steps used:

1. The Core Technique: Bag-of-Words & TF-IDF
   The script doesn't feed raw text directly into the AI. It converts text into numbers using two steps:

CountVectorizer (Bag of Words): It counts how many times every word appears in a document. It ignores grammar and word order, treating the document as a "bag" of words.
TfidfTransformer (TF-IDF): It re-weighs those counts. Words that appear frequently in all documents (like "the", "is") get a lower score, while unique words that distinguish a document get a higher score. 2. The Algorithm: Naive Bayes
MultinomialNB: This is the specific algorithm used for classification. It is based on Bayes' theorem and is very popular for text classification because it's fast and works surprisingly well with word counts (even though it "naively" assumes every word is independent of the others). 3. The Workflow (The Pipeline)
The script bundles these steps into a Pipeline. This ensures that whatever processing we do to the training data (counting words, calculating TF-IDF) is applied exactly the same way to the test data and any future new data.

Tokenize (split text into words using NLTK).
Vectorize (count words).
Transform (apply TF-IDF math).
Classify (predict using Naive Bayes). 4. Optimization: Grid Search (GridSearchCV)
Instead of guessing which settings work best, the script uses Grid Search. It brute-forces through a list of options to find the best combination:

vect**ngram_range: Should it look at single words (1,1) (e.g., "not", "good") or also pairs of words (1,2) (e.g., "not good")?
tfidf**use_idf: Should it use the fancy TF-IDF weighting or just simple counts?
clf\_\_alpha: A smoothing parameter for the Naive Bayes math.
It splits the training data into 5 parts (cv=5), trains on 4, tests on 1, and rotates. This is called Cross-Validation.

Summary of Execution
Loads 2000 movie reviews from your local folder.
Splits them (80% for training, 20% for final testing).
Trains multiple versions of the model (Grid Search) to find the best settings.
Evaluates the winner on the 20% test set (printing accuracy and confusion matrix).
Predicts sentiment for the list of "Fake Reviews" at the bottom.
