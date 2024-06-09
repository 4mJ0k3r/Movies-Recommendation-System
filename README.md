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

The `recommend` function takes a movie title as input and returns the top 5 most similar movies based on the cosine similarity scores. It finds the index of the input movie in the dataframe, calculates the distances (similarity scores) with all other movies, sorts them in descending order, and returns the titles and poster paths of the top 5 movies.

## Streamlit App

The movie recommendation system is integrated into a Streamlit web application. The `app.py` file contains the code for the Streamlit app. Here's an overview of the app:

- The app loads the processed movie data and similarity matrix from the pickle files.
- It displays a dropdown menu for selecting a movie.
- When the "Show Recommendation" button is clicked, it calls the `recommend` function to get the top 5 recommended movies.
- The recommended movie titles and posters are displayed in a grid layout using Streamlit's `columns` feature.
- The `fetch_poster` function is used to retrieve the movie poster images from TMDb API using the movie ID [[1]].

## Dependencies

The following libraries are used in this project:

- NumPy
- Pandas
- NLTK (Natural Language Toolkit)
- scikit-learn
- Streamlit
- requests

Make sure to install these dependencies before running the code.

## Usage

1. Ensure that the required CSV files (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) are in the same directory as the code files.
2. Run the preprocessing code to generate the pickle files (`movie_dict.pkl` and `similarity.pkl`).
3. Run the Streamlit app using the command: `streamlit run app.py`.
4. Access the app in your web browser at the provided URL.
5. Select a movie from the dropdown menu and click the "Show Recommendation" button to see the top 5 recommended movies.

Feel free to explore and modify the code to suit your needs!
