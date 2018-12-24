# Import libraries
%matplotlib inline
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading ratings file
ratings = pd.read_csv('ratings.csv', encoding='latin-1', 
                      usecols=['userId', 'movieId', 'user_embId', 'movie_embId', 'rating'])
max_userid = ratings['userId'].drop_duplicates().max()
max_movieid = ratings['movieId'].drop_duplicates().max()

# Reading ratings file
#users = pd.read_csv('users.csv', sep='\t', encoding='latin-1', 
                   # usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])

# Reading ratings file
movies = pd.read_csv('movies.csv', encoding='latin-1', 
                     usecols=['movieId', 'title', 'genres'])


                     # Create training set
shuffled_ratings = ratings.sample(frac=1., random_state=RNG_SEED)

# Shuffling users
Users = shuffled_ratings['user_embId'].values
print 'Users:', Users, ', shape =', Users.shape

# Shuffling movies
Movies = shuffled_ratings['movie_embId'].values
print 'Movies:', Movies, ', shape =', Movies.shape

# Shuffling ratings
Ratings = shuffled_ratings['rating'].values
print 'Ratings:', Ratings, ', shape =', Ratings.shape


# Import Keras libraries
from keras.callbacks import Callback, EarlyStopping, ModelCheckpoint
# Import CF Model Architecture
from CFModel import CFModel


# Define constants
K_FACTORS = 100
TEST_USER = 2000 


