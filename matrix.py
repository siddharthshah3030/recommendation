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


sparsity = round(1.0 - len(ratings) / float(n_users * n_movies), 3)
print 'The sparsity level of MovieLens1M dataset is ' +  str(sparsity * 100) + '%'

from scipy.sparse.linalg import svds
U, sigma, Vt = svds(Ratings_demeaned, k = 50)

sigma = np.diag(sigma)



