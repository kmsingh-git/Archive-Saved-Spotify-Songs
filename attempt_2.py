import os
import logging

logger = logging.getLogger('Spotify Archive')
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

logger.debug('The client secret I got from OS Environ: {}'.format(CLIENT_SECRET))

import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

username = input("Enter username: ")

token = util.prompt_for_user_token(username, scope)

if token:
    logger.debug('Received token')
    data = {
        'name' : [],
        'artists' : [],
        'album' : [],
        'ext_url' : [],
        'uri' : []
    }

    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    while results:
        for item in results['items']:
            track = item['track']
            data['artists'].append(' | '.join(map(lambda x: x['name'], track['artists'])))
            data['name'].append(track['name'])
            data['album'].append(track['album']['name'])
            data['ext_url'].append(track['external_urls']['spotify'])
            data['uri'].append(track['uri'])
        if results['next']:
            results = sp.next(results)
        else:
            results = None

    import pandas as pd
    import datetime
    df = pd.DataFrame(data)
    df.to_csv('archived_songs_kms_{}.csv'.format(datetime.date.today()))
    logger.debug('Saved songs to csv')
else:
    logger.error("Can't get token for", username)