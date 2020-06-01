# Archive-Saved-Spotify-Songs
Just a simple script to create a backup of all your saved songs. Saves the songs in a csv file. 
<br> Uses OAuth so you'll be prompted to login on the browser.

<br> Before running the script, set these 3 environment variables:

<br> SPOTIPY_CLIENT_ID
<br> SPOTIPY_CLIENT_SECRET
<br> SPOTIPY_REDIRECT_URI

<p> To know what value to set in each, go to My Dashboard on the Spotify Developer website, create an app. Spotify will generate a client id and secret for you, and you can specify a Redirect_uri in the Settings page. Then, just set these 3 things as environment variables (I did that in my virtualenv activate file, 'export SPOTIPY_CLIENT_ID=...', and in the deactivate function, 'unset SPOTIPY_CLIENT_ID' <-- Do this for all 3.

<br> Once you set these 3 variables, just run the app and follow instructions. 

<p>Cheers
