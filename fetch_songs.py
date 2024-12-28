import sqlite3

# Function to fetch and display all songs from the database
def fetch_songs():
    conn = sqlite3.connect('lyrics_database.db')  # Connect to the database
    cursor = conn.cursor()

    try:
        # Execute the SQL query to fetch all songs (Make sure your table has these columns)
        cursor.execute('SELECT track_name, artist_name, lyrics FROM songs')

        # Fetch all rows
        songs = cursor.fetchall()

        if songs:
            for song in songs:
                track_name, artist_name, lyrics = song
                # Print the song details
                print(f"Track Name: {track_name}, Artist: {artist_name}")
                print(f"Lyrics: {lyrics}\n")
        else:
            print("No songs found in the database.")

    except sqlite3.Error as e:
        print(f"Error fetching songs from the database: {e}")

    finally:
        conn.close()  # Close the database connection

# Example usage
fetch_songs()
