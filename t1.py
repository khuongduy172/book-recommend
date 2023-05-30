import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the book dataset
book_data = pd.read_csv('my_books.csv', on_bad_lines = 'skip')

# Preprocess data (example: lowercase book titles and remove punctuation)
book_data['name'] = book_data['name'].str.lower()
book_data['name'] = book_data['name'].str.replace('[^\w\s]', '')

# Initialize and fit TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()
book_features = tfidf_vectorizer.fit_transform(book_data['name'].values.astype('U'))

# Calculate cosine similarity between book features
cosine_sim = cosine_similarity(book_features)

# Function to get recommendations based on a given book
def get_recommendations(book_title, top_n=5):
    # Preprocess input book title
    processed_title = book_title.lower().replace('[^\w\s]', '')

    # Transform input title using TF-IDF vectorizer
    title_features = tfidf_vectorizer.transform([processed_title])

    # Calculate cosine similarity between input title and book features
    cosine_similarities = cosine_similarity(title_features, book_features).flatten()

    # Sort and get top similar books
    top_similar_books = sorted(list(enumerate(cosine_similarities)), key=lambda x: x[1], reverse=True)[1:]

    # Retrieve recommended book titles
    recommended_books = []
    seen_books = set()  # Track seen books to avoid duplicates

    for book in top_similar_books:
        book_index = book[0]
        book_title = book_data.iloc[book_index]['name']
        book_id = book_data.iloc[book_index]['id']
        
        if book_title not in seen_books:
            recommended_books.append({'title': book_title, 'id': str(book_id)})
            seen_books.add(book_title)

        if len(recommended_books) >= top_n:
            break

    return recommended_books[:top_n]

# Example usage
# book_title = 'The Hobbit'
# recommendations = get_recommendations(book_title)
# print(f"Recommended books for '{book_title}':")
# for book in recommendations:
#     print(book)