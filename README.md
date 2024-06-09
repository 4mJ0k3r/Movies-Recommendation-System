# Movie Recommendation System

This is a content-based movie recommendation system built using Python and various data science libraries. It recommends movies to users based on the similarity of movie tags, which include overview, genres, keywords, cast, and crew information.

## Dataset

The system uses two datasets:

- `tmdb_5000_movies.csv`: Contains information about 5000 movies from The Movie Database (TMDb).
- `tmdb_5000_credits.csv`: Contains cast and crew information for the movies.

The datasets are merged based on the movie title to create a single dataframe with relevant columns.

## Preprocessing

Several preprocessing steps are performed on the data:

1. Extracting relevant information from the `genres`, `keywords`, `cast`, and `crew` columns using custom functions.
2. Combining the `overview`, `genres`, `keywords`, `cast`, and `crew` information into a single `tags` column.
3. Applying text preprocessing techniques like splitting, stemming, and removing stop words to the `tags` column.

## Vectorization and Similarity

The preprocessed `tags` are then vectorized using the **CountVectorizer** from scikit-learn, which converts the text data into numerical vectors. The cosine similarity between the movie vectors is calculated to determine the similarity between movies.

## Recommendation

The `recommend` function takes a movie title as input and returns the top 5 most similar movies based on the cosine similarity scores. It finds the index of the input movie in the dataframe, calculates the distances (similarity scores) with all other movies, sorts them in descending order, and returns the titles of the top 5 movies.

## Dependencies

The following libraries are used in this project:

- NumPy
- Pandas
- NLTK (Natural Language Toolkit)
- scikit-learn

Make sure to install these dependencies before running the code.

## Usage

1. Ensure that the required CSV files (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) are in the same directory as the code file.
2. Run the code in a Python environment with the necessary dependencies installed.
3. The processed dataframe and similarity matrix are saved as pickle files (`movie_dict.pkl` and `similarity.pkl`) for future use.
4. Use the `recommend` function by passing a movie title as a string to get recommendations.

Example:
```python
recommend('Batman Begins')
