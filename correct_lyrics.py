def correct_lyrics(lyrics):
    corrections = {
        'mofiill': 'மொழியில்',
        'moliyay': 'மொழியில்',
        'viqiill': 'விழியில்',
        'vivyay': 'விழியில்',
        'urinil': 'உரினில்',
        'pudaitte': 'புதைத்தே',
        'purinditup': 'புரிந்திடுப்',
        'ninheen': 'நின்றேன்',
        'brinden': 'பிரிந்தேன்',
        'anbe': 'அன்பே',
        'dinamum': 'தினமும்',
        'khanavil': 'கனவில்',
        'dolaivil': 'தொலைவில்',
        'kangiheen': 'காங்கிறேன்',
        'athanal': 'அதனால்',
        'iravai': 'இரவை',
        'neela': 'நீள',
        'ketkiren': 'கேட்கிறேன்',
        'eduttu': 'எடுத்து',
        'piraiyal': 'பிறையில்',
        'kavidhai': 'கவிதை',
        'aanadhe': 'ஆனதே',
        'enekke': 'எனக்கு',
        'ethri': 'எதிரி',
        'idhayam': 'இதயம்',
        'madapatill': 'மடவந்தால்',
        'nenche': 'நெஞ்சே',
        'o nenche nenche': 'ஓ நெஞ்சே நெஞ்சே',
        'ninan': 'நிஜம்'
        # Add more corrections as needed
    }

    for incorrect, correct in corrections.items():
        lyrics = lyrics.replace(incorrect, correct)

    return lyrics

def save_corrected_lyrics(track_name, artist_name, lyrics):
    # Correct the lyrics
    corrected_lyrics = correct_lyrics(lyrics)
    
    # Save to a new file
    filename = f"{track_name}_{artist_name}_corrected.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(corrected_lyrics)
    
    print(f"Corrected lyrics saved to {filename}")

# Example usage
track_name = "Marappadhilai Nenjai"
artist_name = "Leon James"
lyrics = """
Mozhiyillai Mozhiyaai
Un Per Sollaamal
Vizhiyillai Vizhiyaai
Un Mugam Paarkaamalll...

Uyirinil Unaiye
Naan Pudhaiththe Nindren
Purindhidum Munne
Unai Pirindhen Anbe

Nidhamum Kanavil
Unai Tholaivil Kaangiren
Adhanaal Iravai Naan Neela Ketkiren

Ezhuthu Pizhayai
En Kavidhai Aanadhey
Enakke Edhiri En Idhayam Aanadhey


Marappadhillai Nenje Nenje Oh Oh
Nenje Nenje Oh Oh
Nenjil Innum Neeyadiii...

Marappadhillai Nenje Nenje Oh Oh
Nenje Nenje Oh Oh
Nenjil Innum Neeyadiii

Oh Oh
Oh Oh

"""  # Example incorrect lyrics

# Save the corrected lyrics to a file
save_corrected_lyrics(track_name, artist_name, lyrics)


def read_corrected_lyrics_file(track_name, artist_name):
    filename = f"{track_name}_{artist_name}_corrected.txt"
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            corrected_lyrics = f.read()
            print(f"Corrected Lyrics for {track_name} by {artist_name}:\n\n{corrected_lyrics}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Example usage
track_name = "Marappadhilai Nenjai"
artist_name = "Leon James"
read_corrected_lyrics_file(track_name, artist_name)
