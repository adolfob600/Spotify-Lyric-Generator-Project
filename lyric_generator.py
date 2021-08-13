from flask import Flask, render_template, url_for, flash, redirect, request
from flask_behind_proxy import FlaskBehindProxy
import time, random, threading
from turbo_flask import Turbo
from spotify_playlists import get_playlist, get_duration
from genius_lyrics import get_lyrics
from youtube_url import get_youtube_url
import cgi

app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '0180308931ad2b57c57125ed08e3ace2'

turbo = Turbo(app)

@app.route("/")

@app.route("/home", methods=['GET', 'POST'])
def home(): 
    if request.method == 'POST': 
      return redirect(url_for("lyric_generator"))
    return render_template('home.html', subtitle='Enter the link to your Spotify playlist to get started!')

@app.route("/lyrics", methods=['GET', 'POST'])
def lyric_generator():

    if request.method == 'POST':
        playlist_link = str(request.form.get('link'))
        dict = get_playlist(playlist_link)
        duration = get_duration(playlist_link)
        index = 0
        songs = []
        text = []
        youtube_urls = []
        for song in dict:
            artists = ""
            if len(dict[song]) > 1:
                print(dict[song])
                for artist in range(len(dict[song])):
                    artists += dict[song][artist] + " "
            else:
                print(dict.get(song)[0])
                artists += str(dict.get(song)[0]) + " "
            songs.append(song + " " + artists) 
        for song in songs:
            text.append(get_lyrics(song))
            youtube_urls.append(get_youtube_url(song + "music video"))
        for url in range(len(youtube_urls)):
            inFile = False
            file = open(".guides/content/Page-1-0ed6.md", "r")
            string = "\n<iframe width=\"560\" height=\"315\" src=\'" + youtube_urls[url] + "\' title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay=1; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"
            for line in file:
                if string in line:
                    inFile = True
            file.close()
            if inFile == False:
                file = open(".guides/content/Page-1-0ed6.md", "a")
                file.write(string)
                file.close()
                print(youtube_urls[url])

        return render_template('lyrics.html', subtitle='Generating lyrics for your playlist...', lyrics=text[0], youtube_url=youtube_urls[0])
    return render_template('lyrics.html', subtitle='Go back to the home page and enter a playlist!')

# @app.context_processor
# def inject_load():
#     if index < len(text):
#         return {'video':(youtube_urls[index]), 'load':text[index]}
      
# @app.before_first_request
# def before_first_request():
#     threading.Thread(target=update_page).start()
    
# def update_page():
#     with app.app_context():
#         while index < len(text):
#             if index is 0:
#                 time.sleep(0)
#             else:
#                 time.sleep(duration[index-1])
#             turbo.push(turbo.replace(render_template('lyrics.html'), 'video'))
#             turbo.push(turbo.replace(render_template('lyrics.html'), 'load'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")