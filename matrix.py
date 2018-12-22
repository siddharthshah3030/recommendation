# Import libraries
import numpy as np
import pandas as pd

# Reading ratings file
ratings = pd.read_csv('dataset/ratings.csv', encoding='latin-1', usecols=['userId', 'movieId', 'rating', 'timestamp'])

# Reading users file
users = pd.read_csv('dataset/users.csv', encoding='latin-1', usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])

# Reading movies file
movies = pd.read_csv('dataset/movies.csv', encoding='latin-1', usecols=['movieId', 'title', 'genres'])

movies.head()

ratings.head()

n_users = ratings.userId.unique().shape[0]
n_movies = ratings.movieId.unique().shape[0]


Ratings = ratings.pivot(index = 'userId', columns ='movieId', values = 'rating').fillna(0)
Ratings.head()

R = Ratings.as_matrix()
user_ratings_mean = np.mean(R, axis = 1)
Ratings_demeaned = R - user_ratings_mean.reshape(-1, 1)