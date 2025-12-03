import pandas as pd
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB

# --- Part 1: Vector Space Conversion (Pages 3-5) ---

# Defining the document collection Z
d1 = "The sky is blue."
d2 = "The sun is bright."
d3 = "The sun in the sky is bright."
d4 = "We can see the shining sun, the bright sun."
Z = (d1, d2, d3, d4)

# Creating the CountVectorizer
# Note: The text initializes it once, then re-initializes with custom vocab
vectorizer = CountVectorizer()
print(vectorizer)

# Defining custom stop words and vocabulary
my_stop_words = {"the", "is"}
my_vocabulary = {'blue': 0, 'sun': 1, 'bright': 2, 'sky': 3}

# Re-initializing with custom parameters
vectorizer = CountVectorizer(stop_words=my_stop_words, vocabulary=my_vocabulary)

print(vectorizer.vocabulary)
print(vectorizer.stop_words)

# creating the sparse matrix of the document set
smatrix = vectorizer.transform(Z)
print(smatrix)

# converting to dense format
matrix = smatrix.todense()
print(matrix)


# --- Part 2: TF-IDF Transformation (Pages 7-8) ---

# Initializing TfidfTransformer
# Text says norm="12", but this is a typo for "l2"
tfidf_transformer = TfidfTransformer(norm="l2") 
tfidf_transformer.fit(smatrix)

# Print IDF values
feature_names = vectorizer.get_feature_names_out() # Updated from get_feature_names() for compatibility
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=feature_names, columns=["idf_weights"])


# sort ascending
print(df_idf.sort_values(by=['idf_weights']))

# Computing TF-IDF scores
tf_idf_vector = tfidf_transformer.transform(smatrix)

# get tfidf vector for first document "The sky is blue."
first_document = tf_idf_vector[0]

# print the scores
df = pd.DataFrame(first_document.T.todense(), index=feature_names, columns=["tfidf"])
print(df.sort_values(by=["tfidf"], ascending=False))


# --- Part 3: Document Similarity (Pages 11-12) ---

# Using TfidfVectorizer (combines CountVectorizer and TfidfTransformer)
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(Z)
print(tfidf_matrix.shape)

# Calculate cosine similarity between first doc and others
cos_similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix)
print(cos_similarity)

# Calculate angle between first and third documents
# Note: cos_similarity returns a 2D array, so we access [0][2] for the 3rd doc
angle_in_radians = math.acos(cos_similarity[0][2])
print(math.degrees(angle_in_radians))


# --- Part 4: Classifying Text with Naive Bayes (Pages 13-16) ---

# Fetch data
data = fetch_20newsgroups()
# print(data.target_names) # Optional based on text

# Define categories and fetch subsets
my_categories = ['rec.sport.baseball', 'rec.motorcycles', 'sci.space', 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=my_categories)
test = fetch_20newsgroups(subset='test', categories=my_categories)

print(len(train.data))
print(len(test.data))
print(train.data[9])

# Create sparse tf-idf matrix for training data
cv = CountVectorizer()
X_train_counts = cv.fit_transform(train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# Create and fit the Multinomial Naive Bayes model
model = MultinomialNB().fit(X_train_tfidf, train.target)

# Apply the model to new documents
docs_new = [
    'Pierangelo is a really good baseball player', 
    'Maria rides her motorcycle', 
    'OpenGL on the GPU is fast', 
    'Pierangelo rides his motorcycle and goes to play football since he is a good football player too.'
]

X_new_counts = cv.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = model.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, train.target_names[category]))