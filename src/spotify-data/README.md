# spotify-data

To run the script to generate the `song_metadata.csv` file from the `song_survey_responses.csv` file:

1. Complete the setup instructions in the root README.md file.
2. Make a copy of `.env.template` called `.env` and replace the dummy values with your [Spotify Web API client ID and client secret](https://developer.spotify.com/documentation/web-api/tutorials/getting-started).
3. Run the command below which will generate `song_metadata.csv`:

```sh
uv run python3 request_data.py
```
