import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess the data
data = pd.read_csv('my_books.csv', on_bad_lines = 'skip')
# Perform any necessary data cleaning and preprocessing steps
# Concatenate relevant attributes into a single string
data['book_content'] = data['name'] + ' ' + data['description']

# Remove any unwanted characters or formatting
data['book_content'] = data['book_content'].str.lower().str.replace(r'\|', ' ')

# Feature extraction
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(data['book_content'].values.astype('U'))

# Calculate the cosine similarity matrix
similarity_matrix = cosine_similarity(feature_matrix, feature_matrix)

def get_top_recommendations(item_id, similarity_matrix, N=5):
    item_index = data[data['id'] == item_id].index[0]
    similarity_scores = similarity_matrix[item_index]
    top_indices = similarity_scores.argsort()[::-1][1:N+1]
    top_items = data.loc[top_indices]['name']
    return top_items

# Example usage
target_item_id = 231
recommendations = get_top_recommendations(target_item_id, similarity_matrix)
print(recommendations)