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
