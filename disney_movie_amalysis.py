# -*- coding: utf-8 -*-
"""Disney -movie-amalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YW3cjvrmhT92zE0MgF_5FghDEKiUk4Ey

# Disney Studio Income Analysis

Since the 1930s, Walt Disney Studios has released more than 600 films covering a wide range of genres. While some movies are indeed directed towards kids, many are intended for a broad audience. In this project, you will analyze data to see how Disney movies have changed in popularity since its first movie release.

# Data

The dataset include all movies produced until 2016.

Available features:


1.   Movie Title
2.   Release Date
3.   Genre
4.   MPAA Rating
5.   Total Gross
6.   Inflation Adjusted Gross

# Import
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

"""# Read the data"""

disney_movies_df = pd.read_csv("/content/disney_movies.csv")

"""# Explore the data"""

disney_movies_df.head()

"""# Checking null values"""

newdf = disney_movies_df.isnull()
newdf

print(f'There are {disney_movies_df.shape[0]} movies included in the dataset. ')

print(f"The oldest movie was released in {disney_movies_df['release_date'].min()}.")

print(f"The newest movie was released in {disney_movies_df['release_date'].max()}.")

disney_movies_df.sort_values(by='release_date')['movie_title'].head(1) # oldest movie

disney_movies_df.sort_values(by='release_date')['movie_title'].tail(1) # newest movie

disney_movies_df.info()

"""# best and worst total gross"""

a = disney_movies_df['total_gross']
min1 = a.min()
min1

a = disney_movies_df['total_gross']
max1 = a.max()
max1

"""# Visualize Year Distribution Plot"""

sns.pairplot(disney_movies_df)

import seaborn as sns

# to ignore the warnings 
from warnings import filterwarnings

sns.distplot(disney_movies_df['total_gross'], kde = False, color ='red', bins = 30)

"""# Does Movies Income Decreased or Increased?"""

sns.lineplot(x="release_date", y="total_gross", data=disney_movies_df);
plt.show()

plt.figure(figsize = [20,15])

"""From the above lineplot graph we can conclude that the movies income has increased.

# Describe the total counts of Genres
"""

arr = disney_movies_df["genre"].unique()
arr

# pandas count distinct values in column
a = disney_movies_df['genre'].value_counts()

"""There are 13 different counts of generes."""