# -------------------------------------
#   IMPORTS
# -------------------------------------
import os
import nltk
import warnings
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix


# Suppress annoying warning from sklearn about token_pattern
warnings.filterwarnings("ignore", category=UserWarning, module='sklearn.feature_extraction.text')


# Ensure nltk tokenizer is available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

# -------------------------------------
#   LOAD DATASET
# -------------------------------------
# Use the local movie_reviews folder relative to this script
current_dir = os.path.dirname(os.path.abspath(__file__))
moviedir = os.path.join(current_dir, 'movie_reviews')

if not os.path.exists(moviedir):
    print(f"Warning: Directory not found: {moviedir}. Trying relative path...")
    moviedir = 'part2/movie_reviews'

print(f"Loading data from {moviedir}...")
movie = load_files(moviedir, shuffle=True, random_state=42)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    movie.data, movie.target, test_size=0.2, random_state=42
)

# -------------------------------------
#   PIPELINE (Naive Bayes)
# -------------------------------------
pipeline = Pipeline([
    ('vect', CountVectorizer(tokenizer=nltk.word_tokenize)),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])

# -------------------------------------
#   GRID SEARCH (HYPERPARAMETER TUNING)
# -------------------------------------
parameters = {
    'vect__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'clf__alpha': (1e-2, 1e-3, 1.0)
}

gs_clf = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1)
gs_clf.fit(X_train, y_train)

print("\nBest CV score:", gs_clf.best_score_)
print("Best parameters:", gs_clf.best_params_)

# -------------------------------------
#   FINAL MODEL EVALUATION
# -------------------------------------
best_model = gs_clf.best_estimator_

final_acc = best_model.score(X_test, y_test)
print("\nFinal test accuracy:", final_acc)

y_pred = best_model.predict(X_test)

print("\nClassification report:\n")
print(classification_report(y_test, y_pred, target_names=movie.target_names))

print("\nConfusion matrix:")
print(confusion_matrix(y_test, y_pred))

# -------------------------------------
#   FAKE REVIEWS TEST
# -------------------------------------
reviews_new = ['This movie was excellent', 'Absolute joy ride', 
            'Steven Seagal was terrible', 'Steven Seagal shone through.', 
              'This was certainly a movie', 'Two thumbs up', 'I fell asleep halfway through', 
              "We can't wait for the sequel!!", '!', '?', 'I cannot recommend this highly enough', 
              'instant classic.', 'Steven Seagal was amazing. His performance was Oscar-worthy.']

# Predict using the best model found
pred = best_model.predict(reviews_new)

print("\n--- Fake Reviews Classification ---")
for review, category in zip(reviews_new, pred):
    print('%r => %s' % (review, movie.target_names[category]))
