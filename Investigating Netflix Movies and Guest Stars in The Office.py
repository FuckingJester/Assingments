import pandas as pd
import matplotlib.pyplot as plt
# Create the years and durations lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {"years": [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
              "durations": [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
              }

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv("datasets/netflix_data.csv")
# Print the first five rows of the DataFrame
print(netflix_df.head())
# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]

# Print the first five rows of the new DataFrame
print(netflix_movies_col_subset.head())
