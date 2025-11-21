from . import db

class Song:
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


class DatabaseAccessObject:
    def __init__(self):
        self.db = db.get_db()
        self.songs = []

    def get_all_songs(self):
        songs = []
        # BEGIN SOLUTION PROMPT="query = _______"
        query = "SELECT * FROM songs"
        # END SOLUTION

        for row in self.db.execute(query).fetchall():
            song = Song(row['track_name'], row['artist_name'], row['album_name'], row['album_image_url'], row['duration'])
            self.songs.append(song.to_dict())
        return self.songs

    def get_song_by_title_and_artist(self, track_name, artist_name):
        # BEGIN SOLUTION PROMPT="query = _______"
        query = """
                SELECT *
                FROM songs
                WHERE artist_name = ? AND track_name = ?
                """
        # END SOLUTION
        row = self.db.execute(query, (artist_name, song_title)).fetchone()

        # BEGIN SOLUTION PROMPT="if _______:"
        if row is not None:
            # END SOLUTION
            # BEGIN SOLUTION PROMPT="return _______"
            return Song(row['track_name'], row['artist_name'], row['album_name'], row['album_image_url'], round(row['duration']))
            # END SOLUTION