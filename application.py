import pickle
import streamlit as st
import requests
from fuzzywuzzy import process

# ---------------------- CONFIGURATION ----------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
TMDB_URL = "https://api.themoviedb.org/3/movie/"
POSTER_FALLBACK = "https://via.placeholder.com/500x750?text=No+Image"

# ---------------------- HELPER FUNCTIONS ----------------------
@st.cache_data(show_spinner=False)
def fetch_movie_details(movie_id):
    try:
        url = f"{TMDB_URL}{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url)
        data = response.json()
        poster = "https://image.tmdb.org/t/p/w500/" + data.get("poster_path", "")
        return {
            "poster": poster if data.get("poster_path") else POSTER_FALLBACK,
            "rating": data.get("vote_average", "N/A"),
            "genres": ", ".join([g['name'] for g in data.get("genres", [])]) or "N/A"
        }
    except:
        return {"poster": POSTER_FALLBACK, "rating": "N/A", "genres": "N/A"}

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        results = []
        for i in distances[1:6]:  # Top 5 excluding the selected movie
            movie_id = movies.iloc[i[0]].movie_id
            title = movies.iloc[i[0]].title
            details = fetch_movie_details(movie_id)
            results.append({
                "title": title,
                "poster": details["poster"],
                "rating": details["rating"],
                "genres": details["genres"]
            })
        return results
    except Exception as e:
        st.error(f"Error during recommendation: {e}")
        return []

def fuzzy_search(query, choices, limit=5):
    results = process.extract(query, choices, limit=limit)
    return [match[0] for match in results]

# ---------------------- LOAD MODELS ----------------------
try:
    movies = pickle.load(open('model/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('model/similarity.pkl', 'rb'))
except Exception as e:
    st.error(f"❌ Could not load model files: {e}")
    st.stop()

movie_titles = movies['title'].values.tolist()

# ---------------------- UI ----------------------
st.title("🎥 Movie Recommender System")
st.markdown("Get smart movie recommendations with posters, genres, and ratings!")

# Search Input
query = st.text_input("🔍 Type a movie name", "")
suggestions = fuzzy_search(query, movie_titles, limit=5) if query else movie_titles[:5]
selected_movie = st.selectbox("🎬 Select a movie", suggestions)

# Show Recommendations
if st.button("📽️ Show Recommendations"):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.subheader("🍿 Recommended Movies")
        cols = st.columns(5)
        for col, movie in zip(cols, recommendations):
            with col:
                st.image(movie["poster"], use_container_width=True)
                st.markdown(f"**{movie['title']}**")
                st.caption(f"⭐ {movie['rating']} &nbsp;&nbsp; 🎭 {movie['genres']}", unsafe_allow_html=True)
    else:
        st.warning("No recommendations found.")