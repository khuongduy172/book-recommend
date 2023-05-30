from flask import Flask, request, jsonify
from t1 import get_recommendations

app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>Hello, World! hhahaha</h1>"

@app.route('/recommend', methods=['POST'])
def recommend_books():
    data = request.get_json()  # Get JSON data from the request

    # Retrieve the book title from the JSON data
    book_title = data['book_title']

    # Call your recommendation function and get the recommended books
    recommendations = get_recommendations(book_title)

    # Return the recommended books as a JSON response
    return jsonify(recommendations)

if __name__ == "__main__":
#   app.run()
  app.run(debug=True)