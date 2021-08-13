import lyricsgenius as lg
import requests
import config

genius = lg.Genius(config.genius_api_key, skip_non_songs=True, excluded_terms=["(Live)"], remove_section_headers=True)
BASE_URL="https://api.genius.com"
headers={'Authorization': 'Bearer {token}'.format(token=config.genius_api_key)}

def get_lyrics(song):
    try:
        return (genius.search_song(song)).lyrics
    except:
        return "no lyrics found"