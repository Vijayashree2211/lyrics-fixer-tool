import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

# Your Spotify API credentials
client_id = "884f40b6855f4970b711f04ff506eea2"
client_secret = "9af83253129d42d9ac3873406997cbb1"

# Your Genius API token
GENIUS_API_TOKEN = "cTQHdIoitEZKzUAtRfkEeW8aGLFf3gksfbKPsZS8V91cs7_mN_xF9FgT2hS7EPQz"

# Authenticate with Spotify API
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Function to search for a song on Spotify
def search_spotify_song(song_name):
    results = sp.search(q=song_name, type="track", limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        print(f"Track: {track_name}\nArtist: {artist_name}")
        return track_name, artist_name
    else:
        print("Song not found on Spotify!")
        return None, None

# Function to search for lyrics on Genius
def search_genius_lyrics(song_name, artist_name):
    search_url = "https://api.genius.com/search"
    headers = {"Authorization": f"Bearer {GENIUS_API_TOKEN}"}
    
    # Construct the search query
    query = f"{song_name} {artist_name}"
    params = {"q": query}
    response = requests.get(search_url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        hits = data['response']['hits']
        if hits:
            song_url = hits[0]['result']['url']
            print(f"Lyrics URL: {song_url}")
        else:
            print("Song not found on Genius!")
    else:
        print(f"Error: {response.status_code}")

# Main function to get lyrics for a song
def get_song_lyrics(song_name):
    # Search for the song on Spotify
    track_name, artist_name = search_spotify_song(song_name)
    
    if track_name and artist_name:
        # Search for lyrics on Genius
        search_genius_lyrics(track_name, artist_name)

# Example: Get lyrics for a song
get_song_lyrics("Vaanam Paarthen")

