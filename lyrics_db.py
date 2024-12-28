import sqlite3

def create_db():
    conn = sqlite3.connect('lyrics_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            track_name TEXT,
            artist_name TEXT,
            lyrics TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_lyrics_to_db(track_name, artist_name, lyrics):
    # Escape single quotes in track_name, artist_name, and lyrics
    track_name = track_name.replace("'", "''")
    artist_name = artist_name.replace("'", "''")
    lyrics = lyrics.replace("'", "''")  # Escape single quotes in lyrics

    conn = sqlite3.connect('lyrics_database.db')
    cursor = conn.cursor()

    try:
        # Insert song data into the database
        cursor.execute('''
            INSERT INTO songs (track_name, artist_name, lyrics)
            VALUES (?, ?, ?)
        ''', (track_name, artist_name, lyrics))  # Passing the values as a tuple

        conn.commit()
        print("Lyrics saved successfully.")
    except sqlite3.Error as e:
        print(f"Error saving lyrics to database: {e}")
    finally:
        conn.close()

# Example usage
track_name = "Vaanam Paarthen"
artist_name = "Santhosh Narayanan"
lyrics = """நதியென நான் ஓடோடி கடலினில் தினம் தேடினேன்
தனிமையின் வலி தீராதோ
மூச்சுக் காற்று போன பின்பு நான் வாழ்வதோ
தீராத காயம் மனதில் உன்னாலடி ஆறாதடி
வானம் பார்த்தே பழகிய விண்மீன் எங்கோ போக
பாறை நெஞ்சம் கரைகிறதே
 

ஏனோ இன்று தூரம் போனால்
இடப் பக்கம் துடித்திடும் இருதய இசை என
இருந்தவள் அவள் எங்கு போனாளோ
இரு விழி இமை சேராமல் உறங்கிட மடி கேட்கிறேன்
மழையினை கண் காணாமல்
மேகம் பார்த்து பூமி கேட்க நான் பாடினேன்
நீ இல்லா நானோ நிழலை தேடும் நிஜம் ஆனேனடி

வானம் பார்த்தே பழகிய விண்மீன் எங்கோ போக
பாறை நெஞ்சம் கரைகிறதே
 

எங்கும் பார்த்தேன் உந்தன் பிம்பம்
கனவிலும் நினைவிலும் தினம் தினம் வருபவள்
எதிரினில் இனி வர நேராதோ

நதியென நான் ஓடோடி கடலினில் தினம் தேடினேன்
தனிமையின் வலி தீராதோ
தூண்டில் முள்ளில் மாட்டிக் கொண்ட மீன் நானடி
ஏமாறும் காலம் இனி வேண்டாமடி கை சேரடி

வானம் பார்த்தே பழகிய விண்மீன் எங்கோ போக
பாறை நெஞ்சம் கரைகிறதே
"""

create_db()  # Create the database and table if necessary
save_lyrics_to_db(track_name, artist_name, lyrics)  # Save lyrics to the database


# Function to add multiple songs to the database
def add_multiple_songs(songs):
    conn = sqlite3.connect('lyrics_database.db')
    cursor = conn.cursor()

    for song in songs:
        track_name = song['track_name'].replace("'", "''")
        artist_name = song['artist_name'].replace("'", "''")
        lyrics = song['lyrics'].replace("'", "''")  # Escape single quotes in lyrics

        try:
            # Insert song data into the database
            cursor.execute('''
                INSERT INTO songs (track_name, artist_name, lyrics)
                VALUES (?, ?, ?)
            ''', (track_name, artist_name, lyrics))  # Passing the values as a tuple
        except sqlite3.Error as e:
            print(f"Error saving song '{track_name}' to database: {e}")

    conn.commit()
    conn.close()
    print("All songs added successfully.")

# Example usage
songs = [
    {
        "track_name": " Maruvarthai ",
        "artist_name": "Darbukasiva",
        "lyrics": """Maru Vaarthai Paesaathe Madi Meethu Nee Thoongidu Imai Pola Naan Kaakka Kanavaai Nee Maaridu
        """  # Truncated for brevity
    },
    {
        "track_name": "Avalum Naanum",
        "artist_name": "A.R.Rahuman",
        "lyrics": """அவளும் நானும் அமுதும் தமிழும் அவளும் நானும் அலையும் கடலும் """  # Provide lyrics for the second song
    },
    {
        "track_name": "Marappadhilai Nenjai",
        "artist_name": "Leon James",
        "lyrics": """
        mofiill moliyay
        un paer chollamal
        viqiill vivyay
        un mugham parkamal
        urinil unaiye
        naan pudaitte ninheen
        purinditup munne
        unai brinden anbe
        dinamum khanavil
        unai dolaivil kangiheen
        athanal iravai
        naan neela ketkiren eduttu piraiyal
        en kavidhai aanadhe enekke ethri 
        un idhayam aanadhe
        madapatill nenche nenche
        o nenche nenche o nenjil 
        innum niyadi madapatill 
        nenche nenche
       o nenche nenche
       mofiill moliyay
       un paer chollamal
       viqiill vivyay
       un mugham parkamal
       urinil unaiye
       naan pudaitte ninheen
       purinditup munne
       unai brinden anbe
       dinamum khanavil
       unai dolaivil kangiheen
       athanal iravai
       naan neela ketkiren
       eduttu piraiyal
       en kavidhai aanadhe
       enekke ethri
       un idhayam aanadhe
       madapatill nenche nenche
       o nenche nenche
       o nenjil innum niyadi
       madapatill nenche nenche
       o nenche nenche
       o nenjil innum niyadi

        """  # Truncated for brevity
    },
    # Add more songs as needed
]



create_db()  # Create the database and table if necessary
add_multiple_songs(songs)  # Add multiple songs to the database
