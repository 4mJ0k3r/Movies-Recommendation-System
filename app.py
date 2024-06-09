import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):  #This function recommends the top 5 movies based on the cosine similarity between the tags of the
    index = movies[movies['title'] == movie].index[0] #This is the index of the movie in the dataframe
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1]) #This sorts the movies based on the cosine similarity between the tags of the movie and the other movies in the dataframe , and lambda x: x[1] sorts the movies based on the cosine similarity in descending order
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:  #This prints the top 5 movies based on the cosine similarity between the tags of the movie
        movie_id = movies.iloc[i[0]].movie_id  #This is the index of the movie in the dataframe
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names, recommended_movie_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Select a movie', movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])