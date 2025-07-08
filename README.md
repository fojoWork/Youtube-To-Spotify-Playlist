# Youtube-To-Spotify-Playlist
Moves your songs from Youtube Music to a Spotify Playlist


# Dependecies <br>
*google-api-python-client* <br>
*spotipy* <br>


#Step 1

First you need to set up your API Keys. First go to https://cloud.google.com and go to their dashboard. Then create a new project by click the project picker in the top left corner of the screen next to the logo, and then click ''Create new project''. After that name your project anything you want and click Create. Make sure to go back to the project picker and open your new project. Next press the three lines in the top left corner and hover API and Services, then click on library. In the search bar look up Youtube Data API v3. Click on it and add it to your project by pressing enable. After that it should redirect you to another page. On that page click on credentials. When in the credentials page click Create Credentials near the top of the page and select API key. After that it will show you your api key. Make sure to copy that down because thats now your api key. Next is to go to the playlist you want to move songs from and copy its ID. In the url for the playlist look for the string of letters and numbers next to 'list='  That is your playlist ID. Put those two below.


#Step 2

Now you need to go to https://developer.spotify.com/ and login. After that click on your profile and then Dashboard. Click create app in your dash board and it will take you to a customization page. Name your api first, and then your redirect URL to http://127.0.0.1:8888/callback. If this redirect doesnt work for you try some others on port 8888. Dont forget to add a description aswell. Your website is optional however. Press save and then copy your Client ID and click view client secret and copy that too. Have those at the ready. Next input your spotify playlist ID. It is similar to youtubes, but instead of 'list=' its just a / followed by the ID.
