import sqlite3


class Song:
    def __init__(
        self,
        track_name: str,
        artist_name: str,
        album_name: str,
        album_image_url: str,
        duration: int,
    ):
        # BEGIN SOLUTION PROMPT="pass"
        self.track_name = track_name
        self.artist_name = artist_name
        self.album_name = album_name
        self.album_image_url = album_image_url
        self.duration = duration
        # END SOLUTION

    def __eq__(self, other: object):
        # BEGIN SOLUTION PROMPT="pass"
        if type(other) is Song:
            return self.to_dict() == other.to_dict()
        return False
        # END SOLUTION

    # BEGIN SOLUTION
    def to_dict(self):
        return {
            "title": self.track_name,
            "artist": self.artist_name,
            "album": self.album_name,
            "album_cover": self.album_image_url,
            "duration": round(self.duration),
        }

    # END SOLUTION


class DatabaseAccessObject:
    def __init__(self, db: sqlite3.Connection):
        # BEGIN SOLUTION PROMPT="pass"
        self.db = db
        # END SOLUTION

    def get_all_songs(self):
        # BEGIN SOLUTION PROMPT="pass"
        all_songs = []
        query = "SELECT * FROM songs"
        rows = self.db.execute(query).fetchall()
        for row in rows:
            song = Song(
                row["track_name"],
                row["artist_name"],
                row["album_name"],
                row["album_image_url"],
                row["duration"],
            )
            all_songs.append(song.to_dict())
        return all_songs
        # END SOLUTION

    def get_song_by_title_and_artist(self, track_name: str, artist_name: str):
        # BEGIN SOLUTION PROMPT="pass"
        query = """
                SELECT *
                FROM songs
                WHERE track_name = ? AND artist_name = ?
                """
        row = self.db.execute(query, (track_name, artist_name)).fetchone()
        if row:
            return Song(
                row["track_name"],
                row["artist_name"],
                row["album_name"],
                row["album_image_url"],
                round(row["duration"]),
            )
        # END SOLUTION
