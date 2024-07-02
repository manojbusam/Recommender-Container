import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class Recommender:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path,sep='|')
        self.tfidf_matrix = None
        self.cosine_sim = None
        self._prepare_data()

    def _prepare_data(self):
        tfidf = TfidfVectorizer(stop_words='english')
        self.data['description'] = self.data['description'].fillna('')
        self.tfidf_matrix = tfidf.fit_transform(self.data['description'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def get_recommendations(self, title, top_n=5):
        idx = self.data.index[self.data['title'] == title].tolist()[0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]
        movie_indices = [i[0] for i in sim_scores]
        return self.data.iloc[movie_indices]['title'].tolist()

# Example usage
if __name__ == "__main__":
    recommender = Recommender("movies.csv")
    recommendations = recommender.get_recommendations("The Matrix")
    print(recommendations)

