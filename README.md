# Anghami to Spotify Playlist Migration
This Python script allows you to migrate playlists from Anghami to Spotify. 

It utilizes the Spotify API, along with the BeautifulSoup and Spotipy libraries, to fetch the playlist information and copy it to your Spotify account.

## Prerequisites
Before running this script, ensure that you have the following installed on your machine:

1. Python 3.x
2. pip (Python package installer)

Additionally, make sure to install the required dependencies by running the following commands in your command prompt:
> pip install beautifulsoup4

> pip install spotipy

> pip install tqdm

## Getting Started
Follow the steps listed below to begin the playlist migration:

1. Navigate to the playlist (or downloads and likes) you want to duplicate on Anghami's web player. Make sure that all the songs are loaded and viewable by scrolling to the bottom of the playlist.
2. To save a web page as an HTML file, right-click on it and choose "Save As". Keep in mind the location where the HTML file was saved.
3. Log in or register for a new account at Spotify for Developers - https://developer.spotify.com/dashboard/.
4. Once logged in, go to the dashboard and create a new app. This app will allow you to access the Spotify API.
5. After creating the app, copy the "Client ID" and "Client Secret" values. You may need to click on "Show Client Secret" to reveal it.
6. Click on "Edit Settings" for your app and set the "Redirect URI" to http://127.0.0.1:8080. After authentication, Spotify will reroute users to this website.
7. Go to your Spotify account and copy your account username. This will be used to identify your Spotify account during the migration process.
8. Open the `config.ini` file and update the client ID, client secret and username values with the data you just acquired.
9. Run the script.

## Note
If you saved the HTML file in a different location than the script directory, you will need to update the `html_file_path` variable in `config.int` as well.

Also, do not forget to update the `playlist_name` variable with the name of the playlist you want to migrate.

## Acknowledgments
The BeautifulSoup library: https://www.crummy.com/software/BeautifulSoup/

The Spotipy library: https://spotipy.readthedocs.io/