# Archive-Saved-Spotify-Songs
Just a simple script to create a backup of all your saved songs. 
Uses OAuth so you'll have to login on the browser.
Saves the file in a csv.
Requires 3 environment variables:

<br> SPOTIPY_CLIENT_ID
<br> SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI

To do this, you got to My Dashboard on the Spotify Developer website, create an app. Spotify will generate a client id and secret for you, and you can specify a Redirect_uri in the Settings page. Then, just set these 3 things as environment variables (I did that in my virtualenv activate file, 'exporrt SPOTIPY_CLIENT_ID=...', and in the deactivate function, 'unset SPOTIPY_CLIENT_ID' <-- Do this for all 3.

Cheers
