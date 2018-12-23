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