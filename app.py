import streamlit as st
from recommendation import get_moods, recommend_songs

st.set_page_config(page_title="Mood Based Music Recommendation", layout="wide")

st.title("🎵 Mood Based Music Recommendation System")

st.write("Select your mood and get song recommendations.")

# Dropdown list
moods = get_moods()

selected_mood = st.selectbox(
    "Select Your Mood",
    moods
)

if st.button("Recommend Songs"):

    songs = recommend_songs(selected_mood)

    st.success(f"Recommended Songs for '{selected_mood}' Mood")

    for index, row in songs.iterrows():

        st.subheader(row["Song Name"])

        st.write("🎤 Artist :", row["Artist"])

        st.write("🎬 Movie :", row["Movie"])

        st.write("---") 