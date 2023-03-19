from flask import Flask, render_template, Response, jsonify,request,redirect
from flask import Flask, render_template, request
import gunicorn
from camera import *
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
#import jsonresoponse


temp=False
app = Flask(__name__)

# Spotify credentials
client_id = "4e1b1aa17008402ea73f17f55be22e01"
client_secret = "c269e3726b6944eb848daf5e77f24f2a"
# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


app = Flask(__name__)

headings = ("Name","Album","Artist")
df1 = music_rec()
df1 = df1.head(15)
df3=music_rec_hindi()
df3=df3.head(15)

t=0
@app.route('/temp',methods=["GET"])
def temp_varaiable():
    lang=request.args.get('lang')
    print("lang")
    print(lang)
    global temp
    if lang=='en':

     
        temp=False
        gen_table()
        return jsonify({'status': 'ok','ok':True})
    else:
      
        temp=True
        gen_table()
        return jsonify({'status': 'ok','ok':True})
@app.route('/')
def index():
    if temp:
    
        return render_template('index.html', headings=headings, data=df3)
    else:
        print(df1.to_json(orient='records'))
        return render_template('index.html', headings=headings, data=df1)

def gen(camera):
    while True:
        global df1
        frame, df1 = camera.get_frame()
        #make
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
  
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/get_access_token')
def get_access_token():
    access_token = sp_oauth.get_access_token()['access_token']
    return jsonify(access_token=access_token)

    # sp_oauth = SpotifyOAuth(client_id=client_id
    # , client_secret=client_secret
    # , redirect_uri='http://localhost:5000/callback', scope='user-read-playback-state,user-modify-playback-state')

    # # get the access token
    # access_token = sp_oauth.get_access_token()['access_token']

    # # create the Spotipy client object with the access token
    # sp = spotipy.Spotify(auth=access_token)

    # # search for the song
    # results = sp.search(q=f"artist:{artist} track:{song}", type='track')

    # # extract the URI of the first search result
    # uri = results['tracks']['items'][0]['uri']
    
    # # Search for the song on Spotify
    # result = sp.search(q='artist:{} track:{}'.format(artist, song), type='track')
    # if len(result['tracks']['items']) == 0:
    #     return 'Song not found'

    # # Get the URI of the first result
    # uri = result['tracks']['items'][0]['uri']
     # create the SpotifyOAuth object


@app.route("/spotify", methods=["GET"])
def search():
    
    artist = request.args.get('artist')
    song = request.args.get('song')

    sp_oauth = SpotifyOAuth(
        client_id="2d85f4d52de540879eb5dfd87fc8fc43",
        client_secret="4d3a865df4f5432ab6fd27cfbd81c3eb",
        redirect_uri='http://localhost:5000/callback', 
        scope='user-read-playback-state,user-modify-playback-state'
    )

    # get the access token
    access_token = sp_oauth.get_access_token()['access_token']

    # create the Spotipy client object with the access token
    sp = spotipy.Spotify(auth=access_token)

    # search for the song
    results = sp.search(q=f"artist:{artist} track:{song}", type='track')

    if len(results['tracks']['items']) == 0:
        # handle case where no tracks were found
        return "No tracks found for that artist and song"
    else:
        # extract the URI of the first search result
        print(results)
        uri = results['tracks']['items'][0]['uri']
        # redirect to the Spotify web player
        return redirect(f"https://open.spotify.com/track/{uri.split(':')[-1]}")

        
@app.route('/t')
def gen_table():
    if temp==True:
        df3=music_rec_hindi()
        df3=df3.head(15)

        

        return df3.to_json(orient='records')
    else:

         return df1.to_json(orient='records')

if __name__ == '__main__':
    app.debug = True
    ## run on port no 5555
    # app.run(host='http://localhost:5555/', port=5555)
    app.run()






