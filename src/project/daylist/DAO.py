from . import db
class Song:
    # BEGIN SOLUTION PROMPT="def __init__(self, track_name, artist_name, album_name, album_image_url, duration):"
    def __init__(self, track_name, artist_name, album_name, album_image_url, duration):
        self.track_name = track_name
        self.artist_name = artist_name
        self.album_name = album_name
        self.album_image_url = album_image_url
        self.duration = duration

    def to_dict(self):
        return {
            "title": self.track_name,
            "artist": self.artist_name,
            "album": self.album_name,
            "album_cover": self.album_image_url,
            "duration": round(self.duration),
        }
    # END SOLUTION

# BEGIN SOLUTION PROMPT="class DatabaseAccessObject:"
class DatabaseAccessObject:
    def __init__(self):
        self.db = db.get_db()

    def get_all_songs(self):
        all_songs = []
        query = "SELECT * FROM songs"

        for row in self.db.execute(query).fetchall():
            song = Song(row['track_name'], row['artist_name'], row['album_name'], row['album_image_url'], row['duration'])
            all_songs.append(song.to_dict())
        return all_songs

    # def get_song_by_title_and_artist(self, artist_name, track_name):
    #     query = """
    #             SELECT *
    #             FROM songs
    #             WHERE artist_name = ? AND track_name = ?
    #             """
    #     row = self.db.execute(query, (artist_name, track_name)).fetchone()

    #     if row:
    #         return Song(row['track_name'], row['artist_name'], row['album_name'], row['album_image_url'], round(row['duration']))
# END SOLUTION