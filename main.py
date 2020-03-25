import spotipy as sp
import spotipy.util as util
import random

SCOPE = 'user-library-read'
USERNAME = ""
SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost/"

token = util.prompt_for_user_token(USERNAME,
                           SCOPE,
                           client_id=SPOTIPY_CLIENT_ID,
                           client_secret=SPOTIPY_CLIENT_SECRET,
                           redirect_uri=REDIRECT_URI)

if token:
    print(sp.Spotify(auth=token).current_user_saved_tracks()['items'][random.randint(0,19)]['track']['name'])
else:
    print("Couldn't get token")