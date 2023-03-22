from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


ClientID = "Your Client ID"
ClientSecret = "Your Client Secret"

desired_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")


response = requests.get(f"https://www.billboard.com/charts/hot-100/{desired_date}/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

body = soup.select("div .o-chart-results-list-row-container")
titles = [item.select_one("li > #title-of-a-story").get_text().strip() for item in body]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=ClientID,
        client_secret=ClientSecret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

year = desired_date.split("-")[0]
song_uris = []

for song in titles:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        song_uris.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{song} not found on Spotify.")

playlist = sp.user_playlist_create(user=user_id, name=f"{desired_date} Billboard 100 playlist2",
                                   public=False,
                                   description="My first programmatic playlist, yooo!")


add_tracks = sp.playlist_add_items(playlist['id'], ['songs_uri'])

print(add_tracks)

















