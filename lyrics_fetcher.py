import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from bs4 import BeautifulSoup

# Spotify Authentication
def search_spotify_song(song_name):
    client_id = "884f40b6855f4970b711f04ff506eea2"  # Replace with your actual Spotify Client ID
    client_secret = "9af83253129d42d9ac3873406997cbb1"  # Replace with your actual Spotify Client Secret
    
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = Spotify(auth_manager=auth_manager)

    results = sp.search(q=song_name, type="track", limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        return track_name, artist_name
    else:
        print("Song not found on Spotify!")
        return None, None

# Genius Lyrics Search
def search_genius_lyrics(track_name, artist_name):
    genius_token = "cTQHdIoitEZKzUAtRfkEeW8aGLFf3gksfbKPsZS8V91cs7_mN_xF9FgT2hS7EPQz"  # Replace with your Genius API token
    search_url = "https://api.genius.com/search"
    headers = {'Authorization': f'Bearer {genius_token}'}
    
    query = f"{track_name} {artist_name}"
    params = {'q': query}
    
    response = requests.get(search_url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['response']['hits']:
            song_path = data['response']['hits'][0]['result']['path']
            lyrics_url = f"https://genius.com{song_path}"
            return lyrics_url
        else:
            print("Song not found on Genius.")
            return None
    else:
        print("Error fetching data from Genius API.")
        return None

# Fetch Lyrics from Genius
def fetch_lyrics(lyrics_url):
    response = requests.get(lyrics_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        lyrics_div = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-6")
        if not lyrics_div:
            lyrics_div = soup.find("div", class_="lyrics")  # Fallback for older structure
        if lyrics_div:
            lyrics = lyrics_div.get_text(separator="\n")
            return lyrics.strip()
    print("Could not fetch lyrics from the URL.")
    return None

# Save Lyrics to a File
def save_lyrics_to_file(track_name, artist_name, lyrics):
    filename = f"{artist_name} - {track_name}.txt".replace("/", "-").replace("\\", "-")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Track: {track_name}\n")
        file.write(f"Artist: {artist_name}\n\n")
        file.write(lyrics)
    print(f"Lyrics saved to {filename}")

# Main Function to Fetch and Save Lyrics
def get_and_save_lyrics(song_name):
    track_name, artist_name = search_spotify_song(song_name)
    
    if track_name and artist_name:
        lyrics_url = search_genius_lyrics(track_name, artist_name)
        if lyrics_url:
            lyrics = fetch_lyrics(lyrics_url)
            if lyrics:
                save_lyrics_to_file(track_name, artist_name, lyrics)
            else:
                print("Lyrics could not be retrieved.")
        else:
            print("Lyrics not found on Genius.")
    else:
        print("Song not found on Spotify.")

# Start Process for "Shape of You"
get_and_save_lyrics("Vaanam Paarthen")
