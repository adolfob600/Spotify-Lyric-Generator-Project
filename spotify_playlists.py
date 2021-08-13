import requests
import spotipy
import config


def make_playlist_id(playlist_link):    #get playlist id from link
    playlist_id=playlist_link.rpartition('/')[2]
    playlist_id=str(playlist_id).rpartition('?')
    return str(playlist_id[0])
    
    
CLIENT_ID=config.spotify_client_ID
CLIENT_SECRET=config.spotify_client_secret
AUTH_URL='https://accounts.spotify.com/api/token'
response=requests.post(AUTH_URL,{
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
})

response_json=response.json()
access_token=response_json['access_token']
headers={'Authorization': 'Bearer {token}'.format(token=access_token)}
BASE_URL='https://api.spotify.com/v1/'


def get_playlist(playlist_link):
    playlist_id=make_playlist_id(playlist_link)
    r=requests.get(BASE_URL+'playlists/'+playlist_id + '/tracks', headers=headers)  #access the tracks in the playlist
    r_json=r.json()
    #print(r_json)
  
    number_of_tracks=len(r_json['items'])
    playlist = {}

    for track in range(number_of_tracks):  

        song=r_json['items'][track]['track']['name']  #name of the track
        artists = []
        number_of_artists=len(r_json['items'][track]['track']['artists'])
        for artist in range(number_of_artists):     #add all of the artists on the track
            artists.append(r_json['items'][track]['track']['artists'][artist]['name']) 
        playlist[song] = artists
        
    return playlist

def get_duration(playlist_link):
    playlist_id=make_playlist_id(playlist_link)
    print(playlist_id)
    r=requests.get(BASE_URL+'playlists/'+playlist_id + '/tracks', headers=headers)  #access the tracks in the playlist
    r_json=r.json()
    number_of_tracks=len(r_json['items'])
    duration = []
    for track in range(number_of_tracks):
        duration.append(int(r_json['items'][track]['track']['duration_ms'])/1000)
        
    return duration
    #for key in playlist:
    #    print(key," by ", playlist[key])