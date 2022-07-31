from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import pprint

SPOTIFY_ID = ""
SPOTIFY_SECRET = ""
SPOTIFY_REDIRECT_URL = ""

song_list = []

spotify_auth = SpotifyOAuth(client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri=SPOTIFY_REDIRECT_URL, scope="playlist-modify-private", cache_path="token.txt", show_dialog=True)

sp = spotipy.Spotify(auth_manager=spotify_auth)

user = sp.current_user()["id"]

chart_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{chart_date}/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
all_songs = soup.select("li h3")

for song in all_songs[:100]:
    song_list.append(song.getText().strip())

song_uris = []

year = chart_date[:4]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"'{song}' not found.")

# print(song_uris)

playlist = sp.user_playlist_create(user=user, name=f"{chart_date} Top 100", public=False)

# print(playlist["id"])

sp.user_playlist_add_tracks(user=user, playlist_id=playlist["id"], tracks=song_uris)
