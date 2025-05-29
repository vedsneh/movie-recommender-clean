import streamlit as st
import pickle
import pandas as pd
import time
import requests
import gdown
import os

similarity_file_id='18PgFIV3weZ3HaFKjJdte9nDrVO0mpCE3'
similarity_path='similarity.pkl'

if not os.path.exists(similarity_path):
    st.info("Downloading similarity.pkl...")
    gdown.download(id=similarity_file_id, output=similarity_path, quiet=False)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=d329aef9f904b6103b063428029cafa0&language=en-US"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses (4xx/5xx)
        data = response.json()
        poster_path = data.get('poster_path')
        return "https://image.tmdb.org/t/p/w500/" + poster_path if poster_path else "https://via.placeholder.com/500x750?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Poster"


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
FILE_ID = "18PgFIV3weZ3HaFKjJdte9nDrVO0mpCE3"  # ← yahan tumhara actual ID daalo
URL = f"https://drive.google.com/file/d/18PgFIV3weZ3HaFKjJdte9nDrVO0mpCE3/view?usp=sharing"

# Check and download if not already present
if not os.path.exists("similarity.pkl"):
    gdown.download(URL, "similarity.pkl", quiet=False)

# Load after downloading
with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)
st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'You want to watch movies similar to?',
    movies['title'].values
)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])