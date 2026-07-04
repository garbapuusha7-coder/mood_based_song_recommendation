import pandas as pd

# Read dataset
df = pd.read_csv("songs.csv")

# Remove extra spaces
df["mood"] = df["mood"].str.strip()

# Function to get all moods
def get_moods():
    return sorted(df["mood"].unique())

# Function to recommend songs
def recommend_songs(selected_mood):
    songs = df[df["mood"] == selected_mood]
    return songs