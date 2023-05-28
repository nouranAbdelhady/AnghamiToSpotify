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
To get started with the playlist migration, follow the steps below:

1. Open Anghami's web player and navigate to the playlist (or downloads and likes) you want to copy. Scroll to the bottom of the playlist to ensure that all the songs are loaded and visible.
2. Right-click on the web page and select "Save As" to save the page as an HTML file. Remember the path where you saved the HTML file.
3. Go to Spotify for Developers and log in or create a new account. Register your account as a developer account if you haven't done so already.
4. Once logged in, go to the dashboard and create a new app. This app will allow you to access the Spotify API.
5. After creating the app, copy the "Client ID" and "Client Secret" values. You may need to click on "Show Client Secret" to reveal it.
6. Click on "Edit Settings" for your app and set the "Redirect URI" to http://127.0.0.1:8080. This is the URL that Spotify will redirect to after authentication.
7. Go to your Spotify account and copy your account username. This will be used to identify your Spotify account during the migration process.
8. Populate the variables in the code with the information you just gathered (HTML file path, client ID, client secret, redirect URL, username), and run the script.

## Acknowledgments
The BeautifulSoup library: https://www.crummy.com/software/BeautifulSoup/
The Spotipy library: https://spotipy.readthedocs.io/