
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load sample dataset (replace 'sample_ratings.csv' with an actual file if available)
ratings = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 3, 3],
    'item_id': [101, 102, 101, 103, 102, 104],
    'rating': [5, 4, 4, 5, 5, 3]
})

# Create user-item matrix
user_item_matrix = ratings.pivot(index='user_id', columns='item_id', values='rating').fillna(0)

# Train a Nearest Neighbors model
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(user_item_matrix)

# Recommend items for a sample user
sample_user = user_item_matrix.iloc[0].values.reshape(1, -1)
distances, indices = model.kneighbors(sample_user, n_neighbors=3)

print("Recommended items:", indices.flatten())
