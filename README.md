import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load dataset
try:
    ratings = pd.read_csv('data/sample_ratings.csv')
except FileNotFoundError:
    # Sample dataset if no file is found
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

# Function to get recommendations
def get_recommendations(user_id, n_recommendations=3):
    if user_id not in user_item_matrix.index:
        return f"User {user_id} not found in dataset."

    user_vector = user_item_matrix.loc[user_id].values.reshape(1, -1)
    distances, indices = model.kneighbors(user_vector, n_neighbors=n_recommendations + 1)
    
    recommended_users = user_item_matrix.index[indices.flatten()][1:]
    
    recommended_items = set()
    for user in recommended_users:
        recommended_items.update(ratings[ratings["user_id"] == user]["item_id"].tolist())

    return f"Recommended items for User {user_id}: {list(recommended_items)}"

# Example usage
if __name__ == "__main__":
    user_id = int(input("Enter User ID for recommendations: "))
    print(get_recommendations(user_id))
