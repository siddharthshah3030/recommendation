import pandas as pd 
import numpy as np

data = pd.read_csv('ratings.csv')

movie_titles = pd.read_csv('movies.csv')
#movie_titles.head()

#merge movieid with movie name
data = pd.merge(data, movie_titles, on='movieId')
# data.head()
# data.describe()

#getting mean ratin for a movie
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
ratings.head()