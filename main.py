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

#visualize
movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')
movie_matrix.head()

#sorting ratings
ratings.sort_values('number_of_ratings', ascending=False).head(10)

AFO_user_rating = movie_matrix['Air Force One (1997)']
contact_user_rating = movie_matrix['Contact (1997)']
AFO_user_rating.head()
contact_user_rating.head()
similar_to_air_force_one=movie_matrix.corrwith(AFO_user_rating)
similar_to_air_force_one.head()
#movies similar to below name
similar_to_contact = movie_matrix.corrwith(contact_user_rating)
similar_to_contact.head()

corr_contact = pd.DataFrame(similar_to_contact, columns=['Correlation'])
corr_contact.dropna(inplace=True)
corr_contact.head()
corr_AFO = pd.DataFrame(similar_to_air_force_one, columns=['correlation'])
corr_AFO.dropna(inplace=True)
corr_AFO.head()

corr_AFO = corr_AFO.join(ratings['number_of_ratings'])
corr_contact = corr_contact.join(ratings['number_of_ratings'])
corr_AFO .head()
corr_contact.head()

#recommendign top 10 movies 
corr_AFO[corr_AFO['number_of_ratings'] > 100].sort_values(by='correlation', ascending=False).head(10)


corr_contact[corr_contact['number_of_ratings'] > 100].sort_values(by='Correlation', ascending=False).head(10)



