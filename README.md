# README.md

# 🎬 Movie Recommender System

A content-based movie recommender web app built with **Streamlit**, using movie similarity data and **The Movie Database (TMDb)** API to show posters, ratings, and genres for recommended movies.

---

## 🚀 Features

- 🔍 Fuzzy search for movie titles  
- 🎥 Top 5 recommendations with posters  
- 🎭 Genre and ⭐ rating display using TMDb API  
- ⚡ Fast performance with Streamlit caching  
- 🧠 Uses precomputed similarity matrix for content-based filtering  

---

## 🧠 How It Works

1. User searches/selects a movie.  
2. The app finds the most similar movies using a similarity matrix.  
3. For each recommended movie, it fetches:  
   - Poster  
   - Genre  
   - Rating  
   from **TMDb API**.  

---

## 🗂️ Folder Structure

your_project/
├── application.py  
├── model/  
│   ├── movie_list.pkl  
│   └── similarity.pkl  

---

## 🛠️ Installation

# 1. Clone this repository
git clone https://github.com/your-username/movie-recommender.git  
cd movie-recommender  

# 2. Install dependencies
pip install -r requirements.txt  

# 3. Run the app
streamlit run application.py  

---

## 🔑 TMDb API Key

This app uses [The Movie Database (TMDb)](https://www.themoviedb.org/documentation/api) API to fetch movie posters, genres, and ratings.

The current code includes a demo API key. For production use, get your own:

1. Go to https://www.themoviedb.org/settings/api  
2. Create an account and generate an API key  
3. Replace the API_KEY in application.py  

Example:

API_KEY = "your_own_tmdb_api_key"  

---

## 🖼️ Preview

![image](https://github.com/user-attachments/assets/a1d08a4e-91fc-47b3-b3f6-05710edecb5d)

![image](https://github.com/user-attachments/assets/ff3655d8-cc8e-4d30-9640-9a0661b68359)

![image](https://github.com/user-attachments/assets/e6d9710a-e74f-45b1-939c-381602e8ef91)

![image](https://github.com/user-attachments/assets/58ce0113-4703-4c80-aa24-7efd5c3e5d4c)

---

## ✍️ Author

**Chayank Tatavarty**  
