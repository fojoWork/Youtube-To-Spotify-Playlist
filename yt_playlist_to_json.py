import json
from googleapiclient.discovery import build



input("First you need to set up your API Keys. First go to https://cloud.google.com and go to their dashboard. Then create a new project by click the project picker in the top left corner of the screen next to the logo, and then click ''Create new project''. After that name your project anything you want and click Create. Make sure to go back to the project picker and open your new project. Next press the three lines in the top left corner and hover API and Services, then click on library. In the search bar look up Youtube Data API v3. Click on it and add it to your project by pressing enable. After that it should redirect you to another page. On that page click on credentials. When in the credentials page click Create Credentials near the top of the page and select API key. After that it will show you your api key. Make sure to copy that down because thats now your api key. Next is to go to the playlist you want to move songs from and copy its ID. In the url for the playlist look for the string of letters and numbers next to 'list='  That is your playlist ID. Put those two below. Please Press enter if you have done both steps:  ")


# --- CONFIGURATION ---
API_KEY = input("Your API key: ")
PLAYLIST_ID = input("Your playlist ID:  ")
OUTPUT_FILE = 'yt_playlist.json'

# --- SETUP YOUTUBE API CLIENT ---
youtube = build('youtube', 'v3', developerKey=API_KEY)

# --- FUNCTION TO GET ALL VIDEOS IN PLAYLIST ---
def get_playlist_videos(youtube, playlist_id):
    videos = []
    next_page_token = None
    while True:
        pl_request = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        pl_response = pl_request.execute()
        for item in pl_response['items']:
            video_data = {
                'title': item['snippet']['title'],
                'videoId': item['snippet']['resourceId']['videoId'],
                'publishedAt': item['snippet']['publishedAt'],
                'channelTitle': item['snippet']['videoOwnerChannelTitle'] if 'videoOwnerChannelTitle' in item['snippet'] else None
            }
            videos.append(video_data)
        next_page_token = pl_response.get('nextPageToken')
        if not next_page_token:
            break
    return videos

# --- MAIN EXECUTION ---
def main():
    print(f"Fetching videos from playlist: {PLAYLIST_ID}")
    videos = get_playlist_videos(youtube, PLAYLIST_ID)
    print(f"Fetched {len(videos)} videos. Saving to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)
    print("Done!")

if __name__ == '__main__':
    main()