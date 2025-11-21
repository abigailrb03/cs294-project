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

    def __eq__(self, other: object) -> bool:
        # BEGIN SOLUTION PROMPT="pass"
        if type(other) is Song:
            return self.to_dict() == other.to_dict()
        return NotImplemented
        # END SOLUTION

    # BEGIN SOLUTION
    def to_dict(self) -> dict:
        return {
            "title": self.track_name,
            "artist": self.artist_name,
            "album": self.album_name,
            "album_cover": self.album_image_url,
            "duration": round(self.duration),
        }

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return str(self.to_dict())

    # END SOLUTION


class DataAccessObject:
    def __init__(self, db: sqlite3.Connection):
        # BEGIN SOLUTION PROMPT="pass"
        self.db = db
        # END SOLUTION

    def get_all_songs(self) -> list[dict]:
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

    def get_song_by_title_and_artist(
        self, track_name: str, artist_name: str
    ) -> Song | None:
        # BEGIN SOLUTION PROMPT="query = _____"
        query = """
                SELECT *
                FROM songs
                WHERE artist_name = ? AND track_name = ?
                """
        # END SOLUTION

        row = self.db.execute(query, (artist_name, track_name)).fetchone()

        # BEGIN SOLUTION PROMPT="# add the rest of your code here"
        if row:
            return Song(
                row["track_name"],
                row["artist_name"],
                row["album_name"],
                row["album_image_url"],
                round(row["duration"]),
            )
        # END SOLUTION
