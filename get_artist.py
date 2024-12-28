import sqlite3
def search_songs_by_artist(artist_name):
    artist_name = artist_name.replace("'", "''")  # Escape single quotes
    conn = sqlite3.connect('lyrics_database.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT track_name, artist_name, lyrics
            FROM songs
            WHERE artist_name LIKE ?
        ''', ('%' + artist_name + '%',))  # Using LIKE for partial matching

        results = cursor.fetchall()
        if results:
            for row in results:
                print(f"Track: {row[0]}\nArtist: {row[1]}\nLyrics:\n{row[2]}\n")
        else:
            print("No songs found for the given artist name.")
    except sqlite3.Error as e:
        print(f"Error searching for songs: {e}")
    finally:
        conn.close()

# Example usage
search_songs_by_artist("Leon James")
