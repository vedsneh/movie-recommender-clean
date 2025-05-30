# Movie Recommender System 🎬

A simple and interactive movie recommendation web app built with **Streamlit**.  
It suggests movies similar to the one you select, fetching movie posters dynamically from The Movie Database (TMDb) API.

**Live Demo:**

You can check the live version of this Movie Recommender app here: https://movie-recommender-clean-3e35tljumqurxvs7kprujv.streamlit.app/

## Features

- User-friendly interface built with Streamlit
- Recommends 5 movies similar to the selected movie title
- Displays movie posters fetched live from TMDb API
- Uses precomputed similarity scores for fast recommendations
- Handles API errors gracefully and shows placeholder images if poster not found

## How to use
1. Select a movie from the dropdown list.
2. Click the **Recommend** button.
3. View 5 recommended movies along with their posters.

## Tech Stack and Tools
- Python 3.13
- Streamlit (Web app framework)
- Pandas (Data handling)
- Requests (HTTP requests for API calls)
- Pickle (for loading precomputed data, Data serialization)
- gdown (for downloading large files from google drive)
- PyCharm (Development IDE)
- Git & GitHub (Version control)
  
