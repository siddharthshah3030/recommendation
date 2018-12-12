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

# gettign frequency of ratings for a movie
ratings['number_of_ratings'] = data.groupby('title')['rating'].count()
ratings.head()

# visualise ratings
import matplotlib.pyplot as plt
%matplotlib inline
ratings['rating'].hist(bins=50)

ratings['number_of_ratings'].hist(bins=60)

import seaborn as sns
sns.jointplot(x='rating', y='number_of_ratings', data=ratings)