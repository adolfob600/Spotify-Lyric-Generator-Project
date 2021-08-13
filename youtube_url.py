from googleapiclient.discovery import build
import config

API_KEY=config.youtube_api_key
youtube=build('youtube', 'v3', developerKey=API_KEY)

def get_youtube_url(query):
  search = youtube.search().list(part="snippet", type="video", q=query).execute()
  url = "https://www.youtube.com/embed/" + search['items'][0]['id']['videoId'] +"?autoplay=1"
  return url


