import pandas as pd
import os as os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load and preprocess dataset
dirname = os.path.dirname(__file__)
filetname = os.path.join(dirname, '../data/dataset.csv')
books = pd.read_csv(filetname)

# Fit the TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books['description'])

# Compute similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def get_recommendations(preferences):
    # Implement logic to get book indices based on user preferences
    # For simplicity, return top N books
    recommended_books = books.head(10).to_dict('records')
    return recommended_books
