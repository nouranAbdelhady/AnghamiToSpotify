from bs4 import BeautifulSoup
from tqdm import tqdm
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Function to load the details
def load_details():
    # Anghami playlist saved HTML file path
    html_file_path = "./anghami.html"
    # Spotify app details
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    # Jupyter Notebook URL (Don't change this)
    redirect_url = "http://127.0.0.1:8080"
    # Spotify username
    username = "YOUR_USERNAME"
    # Spotify playlist name
    spotify_playlist_name = "YOUR_PLAYLIST_NAME"
    # Whether to save the playlist to a text file or not
    save_to_text = True
    txt_save_path = "./playlist.txt"
    # The separator between the song name and the artist name in the text file
    txt_song_artist_separator = ' - '
    return html_file_path, client_id, client_secret, redirect_url, username, spotify_playlist_name, save_to_text, txt_save_path, txt_song_artist_separator

html_path, client_id, client_secret, redirect_url, username, spotify_playlist_name, save_to_text, txt_save_path, txt_song_artist_separator = load_details()

# Read the HTML file and parse it using BeautifulSoup
with open(html_path, encoding="utf8") as f:
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')

# Find the song titles from the HTML
classLst = ["cell cell-title", "cell cell-title marquee"]
mydivs = soup.find_all("div", class_=classLst)
songs = []
print("\nReading Songs")
for job_element in tqdm(mydivs, bar_format="{l_bar}{bar}{r_bar}"):
    title_element = job_element.find("span")
    songs.append(title_element.text)

# Find the artists from the HTML
mydivsart = soup.find_all("div", {"class": "cell cell-artist"})
artists = []
print("\nReading Artists")
for job_element in tqdm(mydivsart, bar_format="{l_bar}{bar}{r_bar}"):
    artists.append(job_element.text)

# Check if the number of songs matches the number of artists
if len(songs) != len(artists):
    print("\nError: Number of songs and artists do not match.")
else:
    print("\nReading successful")

# Print the songs and artists
print("\nPlaylist Details:")
for i in range(len(songs)):
    print(songs[i] + txt_song_artist_separator + artists[i])

# Save the playlist to a text file
if save_to_text:
    with open(txt_save_path, 'w', encoding="utf8") as fp:
        print("\nSaving playlist to text file...")
        for i in tqdm(range(len(songs)), bar_format="{l_bar}{bar}{r_bar}"):
            # Write each item on a new line
            fp.write(songs[i] + txt_song_artist_separator + artists[i] + '\n')
        print('\nPlaylist saved to text file.')

# Authenticate and create a new playlist on Spotify
scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_url,
                                               scope=scope,
                                               username=username))
sp.user_playlist_create(user=username, name=spotify_playlist_name, public=True, description="Imported from Anghami")

notfound = []
playlist = sp.user_playlists(user=username)['items'][0]['id']

# Search and add tracks to the Spotify playlist
print("\nImporting playlist to Spotify...")
for i in tqdm(range(len(songs)), bar_format="{l_bar}{bar}{r_bar}", colour='green'):
    try:
        res = sp.search(q=songs[i] + " " + artists[i], type='track', limit=1)
    except:
        notfound.append(songs[i] + " " + artists[i])
    else:
        if len(res['tracks']['items']) == 0:
            notfound.append(songs[i] + " " + artists[i])
        else:
            uri = res['tracks']['items'][0]['uri']
            sp.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=[uri])

print('\nPlaylist import completed.')

if len(notfound) > 0:
    print('\nThe following songs could not be found on Spotify:')
    for song in notfound:
        print(song)
