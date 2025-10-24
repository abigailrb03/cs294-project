# spotify_webscrape

To run the script to generate the `song_metadata.csv` file from the `songs.csv` file:

1. Make a copy of `.env.template` called `.env` and replace the dummy values with your [Spotify Web API client ID and client secret](https://developer.spotify.com/documentation/web-api/tutorials/getting-started).
2. Run `python3 request_data.py`, which will generate `song_metadata.csv`
