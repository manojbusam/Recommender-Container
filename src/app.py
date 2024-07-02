from flask import Flask, request, jsonify
from recommender import Recommender

app = Flask(__name__)

recommender = Recommender("movies.csv")

@app.route('/recommend', methods=['GET'])
def recommend():
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Title parameter is required"}), 400
    recommendations = recommender.get_recommendations(title)
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

