import json
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

input("Now you need to go to https://developer.spotify.com/ and login. After that click on your profile and then Dashboard. Click create app in your dash board and it will take you to a customization page. Name your api first, and then your redirect URL to http://127.0.0.1:8888/callback. If this redirect doesnt work for you try some others on port 8888. Dont forget to add a description aswell. Your website is optional however. Press save and then copy your Client ID and click view client secret and copy that too. Have those at the ready. Next input your spotify playlist ID. It is similar to youtubes, but instead of 'list=' its just a / followed by the ID. If you have all these three please proceed:  ")

# --- CONFIGURATION ---
SPOTIPY_CLIENT_ID =   input("Please input your CLIENT ID:  ")
SPOTIPY_CLIENT_SECRET = input("Please input your CLIENT SECRET:  ")
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8888/callback'
SPOTIFY_PLAYLIST_ID = input("Please input your spotify playlist ID:  ")
YT_JSON_FILE = 'yt_playlist.json'  # Path to your YouTube playlist JSON

# --- SETUP SPOTIPY CLIENT ---
scope = 'playlist-modify-public playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope
))

def search_track(sp, title, artist=None):
    query = f'track:{title}'
    if artist:
        query += f' artist:{artist}'
    results = sp.search(q=query, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        return tracks[0]['id']
    return None

def main():
    with open(YT_JSON_FILE, 'r', encoding='utf-8') as f:
        yt_tracks = json.load(f)

    track_ids = []
    for entry in yt_tracks:
        title = entry.get('title')
        artist = entry.get('channelTitle')
        track_id = search_track(sp, title, artist)
        if not track_id and artist:
            # Try searching without artist if not found
            track_id = search_track(sp, title)
        if track_id:
            print(f"Found: {title} - {artist}")
            track_ids.append(track_id)
        else:
            print(f"Not found: {title} - {artist}")
        time.sleep(0.2)  # To avoid rate limits

    # Add tracks to Spotify playlist in batches of 100
    for i in range(0, len(track_ids), 100):
        batch = track_ids[i:i+100]
        sp.playlist_add_items(SPOTIFY_PLAYLIST_ID, batch)
        print(f"Added {len(batch)} tracks to playlist.")

    print("All done!")

if __name__ == '__main__':
    main() 