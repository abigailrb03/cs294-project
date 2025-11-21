from flask import Blueprint, jsonify, request
from http import HTTPStatus
import random
from .DAO import DatabaseAccessObject

from . import db

# Create the api Blueprint
bp = Blueprint("api", __name__)

DEFAULT_SEED = 88
NUM_SONGS_IN_DAYLIST = 50


@bp.route("/api/track-image", methods=["GET"])
def track_image():
    """
    Endpoint: GET /api/track-image

    Request query parameters:
        artist (str): Artist name
        title (str): Song title

        Example URL: http://127.0.0.1:5000/api/track-image?artist=Taylor%20Swift&title=Elizabeth%20Taylor

    Response format: JSON object with artist name, song title, and album cover image URL.
        Example below with fake data:

        {
            "artist": "Taylor Swift",
            "title": "Elizabeth Taylor",
            "image_url": "https://example.jpg"
        }
    """
    # BEGIN SOLUTION PROMPT="artist_name = _______"
    artist_name = request.args.get("artist", default=None)
    # END SOLUTION
    # BEGIN SOLUTION PROMPT="song_title = _______"
    song_title = request.args.get("title", default=None)
    # END SOLUTION

    # BEGIN SOLUTION PROMPT="if _______:"
    if artist_name is None or song_title is None:
        # END SOLUTION
        # BEGIN SOLUTION PROMPT="return jsonify({'YOUR ANSWER HERE': 'AS A DICTIONARY'}), HTTPStatus._______"
        return jsonify(
            {
                "status": "error",
                "message": "Artist name and/or song title not provided as query arguments, both are required",
            }
        ), HTTPStatus.BAD_REQUEST
        # END SOLUTION

    database = db.get_db()
    # BEGIN SOLUTION PROMPT="query = _______"
    query = """
            SELECT album_image_url
            FROM songs
            WHERE artist_name = ? AND track_name = ?
            """
    # END SOLUTION
    row = database.execute(query, (artist_name, song_title)).fetchone()

    # BEGIN SOLUTION PROMPT="if _______:"
    if row is None:
        # END SOLUTION
        # BEGIN SOLUTION PROMPT="return jsonify({'YOUR ANSWER HERE': 'AS A DICTIONARY'}), HTTPStatus._______"
        return jsonify(
            {
                "status": "error",
                "message": f"Track image for artist {artist_name} and song title {song_title} not found",
            }
        ), HTTPStatus.NOT_FOUND
        # END SOLUTION

    # BEGIN SOLUTION PROMPT="return jsonify({'YOUR ANSWER HERE': 'AS A DICTIONARY'}), HTTPStatus._______"
    return jsonify(
        {
            "artist": artist_name,
            "title": song_title,
            "image_url": row["album_image_url"],
        }
    ), HTTPStatus.OK
    # END SOLUTION


@bp.route("/api/daylist", methods=["GET"])
def daylist():
    """
    Endpoint: GET /api/daylist

    Request query parameters:
        seed (int): Pseudorandom number generator seed. Optional and defaults to `DEFAULT_SEED`

        Example URLs:
            http://127.0.0.1:5000/api/daylist
            http://127.0.0.1:5000/api/daylist?seed=42

    Response format: JSON object with playlist title, playlist cover image, and a playlist.

    A playlist is a list of songs with `NUM_SONGS_IN_DAYLIST` songs sampled from the database.
    Each song is stored as a dictionary, which contains the following keys:
    song title, artist name, album, album cover image URL, and duration (rounded to the nearest second).

        Example song below with fake data:

        {
            "title": "Love Me Not",
            "artist": "Ravyn Lenae",
            "album": "Bird's Eye",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273ef985ba96e76a9574cc68a30",
            "duration": 156,
        }
    """
    result = {
        "title": "manic pixie dream girl monday",
        "image": "https://img.freepik.com/premium-photo/blue-neon-color-gradient-horizontal-background_653449-8801.jpg",
        "playlist": [],
    }

    # BEGIN SOLUTION PROMPT="database = _______"
    database = DatabaseAccessObject()
    # END SOLUTION
    # BEGIN SOLUTION PROMPT="all_songs = _______"
    all_songs = database.get_all_songs()
    # END SOLUTION

    # BEGIN SOLUTION PROMPT="seed = _______"
    seed = request.args.get("seed", default=DEFAULT_SEED)
    # END SOLUTION
    random.seed(seed)

    # BEGIN SOLUTION PROMPT="chosen_songs = _______"
    chosen_songs = random.sample(all_songs, NUM_SONGS_IN_DAYLIST)
    # END SOLUTION

    # BEGIN SOLUTION PROMPT="result = _______"
    result["playlist"] = chosen_songs
    # END SOLUTION

    # BEGIN SOLUTION PROMPT="return = _______"
    return jsonify(result), HTTPStatus.OK
    # END SOLUTION
