import pandas as pd
import requests
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

songs_df = pd.read_csv("./song_survey_responses.csv")
songs_df.rename(
    columns={
        songs_df.columns[0]: "time",
        songs_df.columns[1]: "email",
        songs_df.columns[2]: "song_link",
    },
    inplace=True,
)
songs_df["song_id"] = songs_df["song_link"].str.extract(r"\/track\/(.+)\?")

client_id = env_vars["SPOTIFY_CLIENT_ID"]
client_secret = env_vars["SPOTIFY_CLIENT_SECRET"]

auth_url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}

response = requests.post(auth_url, data=data, auth=(client_id, client_secret))

if response.status_code == 200:
    access_token = response.json()["access_token"]
    print("Access token:", access_token)
else:
    print("Error:", response.status_code, response.text)


song_metadata_df = songs_df[["song_link", "song_id"]]
song_metadata_df["track_name"] = None
song_metadata_df["artist_name"] = None
song_metadata_df["album_image_url"] = None

headers = {"Authorization": f"Bearer {access_token}"}

for idx, song_id in enumerate(song_metadata_df["song_id"]):
    url = f"https://api.spotify.com/v1/tracks/{song_id}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        song_metadata_df.loc[idx, "track_name"] = data["name"]
        song_metadata_df.loc[idx, "artist_name"] = data["artists"][0]["name"]
        song_metadata_df.loc[idx, "album_image_url"] = data["album"]["images"][0]["url"]

    else:
        print(f"Error fetching {song_id}: {response.status_code}")

song_metadata_df.to_csv("song_metadata.csv", index=False)
