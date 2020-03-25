import spotipy as sp
import spotipy.util as util
import random

SCOPE = 'user-library-read'
USERNAME = "ksingh1993"
SPOTIPY_CLIENT_ID = "7788d7cbcbb7495caac606155c8c5184"
SPOTIPY_CLIENT_SECRET = "17aefb97a4734931a95e2cb7cb3494b8"
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