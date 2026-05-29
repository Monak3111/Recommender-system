import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:



    def __init__(self):
        self.df= pd.read_csv("data.csv")
        self.matrix=None
        self.similarity= None

    def build(self):
        weights: {"view" : 1, "click" : 2, "purcchase" : 3}
        self.df["score"]= self.df["action"].map(weights)

        matrix = self.df.pivot_table(
            index="user_id",
            columns="item_id",
            values="score",
            aggfunc="sum",
            fill_value=0,
        )

        self.matrix= matrix
        self.similarity= cosine_similarity(matrix)

    def recommend(self, user_id, top_k=5):
        if self.matrix is None:
            self.build()

        if user_id not in self.matrix.index:
            return []

        idx = list(self.matrix.index).index(user_id)
        sim = self.similarity[idx]

        similar_users = sim.argsort()[::-1][1:3]

        scores = self.matrix.iloc[similar_users].mean().sort_values(ascending=False)

        return list(scores.head(top_k).index)