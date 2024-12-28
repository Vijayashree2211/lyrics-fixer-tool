import sqlite3
import streamlit as st

# Function to fetch unique songs from the database
def fetch_unique_songs():
    conn = sqlite3.connect('lyrics_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT track_name, artist_name FROM songs")  # Ensuring no duplicates
    songs = cursor.fetchall()
    conn.close()
    return songs

# Function to fetch lyrics for a specific song
def fetch_song_lyrics(track_name, artist_name):
    conn = sqlite3.connect('lyrics_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT lyrics FROM songs WHERE track_name = ? AND artist_name = ?", (track_name, artist_name))
    lyrics = cursor.fetchone()
    conn.close()
    return lyrics[0] if lyrics else None

# Function to fetch corrected lyrics from file
def get_corrected_lyrics(track_name, artist_name):
    filename = f"{track_name}_{artist_name}_corrected.txt"
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            corrected_lyrics = f.read()
            return corrected_lyrics
    except FileNotFoundError:
        return None

# Streamlit UI layout
st.set_page_config(page_title="Lyrics Database and Correction Tool", layout="wide")
st.title("🎶 Lyrics Database and Correction Tool")

# Sidebar for selecting a song
st.sidebar.title("Select a Song")
songs = fetch_unique_songs()

if songs:
    selected_song = st.sidebar.selectbox("Choose a song", songs, format_func=lambda song: f"{song[0]} by {song[1]}")

    if selected_song:
        track_name, artist_name = selected_song

        # Display Original Lyrics
        st.subheader(f"Original Lyrics for '{track_name}' by {artist_name}")
        original_lyrics = fetch_song_lyrics(track_name, artist_name)
        if original_lyrics:
            st.text_area("Original Lyrics", original_lyrics, height=200, key="original")
        else:
            st.warning("Original lyrics not found in the database.")

        # Display Corrected Lyrics
        st.subheader(f"Corrected Lyrics for '{track_name}' by {artist_name}")
        corrected_lyrics = get_corrected_lyrics(track_name, artist_name)
        if corrected_lyrics:
            st.text_area("Corrected Lyrics", corrected_lyrics, height=200, key="corrected")
        else:
            st.warning("Corrected lyrics not found.")
else:
    st.sidebar.error("No songs found in the database.")

# Adding new lyrics
st.sidebar.title("Add New Lyrics")
new_track_name = st.sidebar.text_input("Track Name")
new_artist_name = st.sidebar.text_input("Artist Name")
new_lyrics = st.sidebar.text_area("Lyrics", height=200)
if st.sidebar.button("Add Lyrics"):
    if new_track_name and new_artist_name and new_lyrics:
        conn = sqlite3.connect('lyrics_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO songs (track_name, artist_name, lyrics)
            VALUES (?, ?, ?)
        ''', (new_track_name, new_artist_name, new_lyrics))
        conn.commit()
        conn.close()
        st.sidebar.success(f"Lyrics for '{new_track_name}' by {new_artist_name} added successfully!")
    else:
        st.sidebar.error("Please fill out all fields.")
