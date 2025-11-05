from flask import Blueprint, jsonify, request
from http import HTTPStatus
from random import sample

from . import db

# Create the api Blueprint
bp = Blueprint("api", __name__)

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
        # BEGIN SOLUTION PROMPT="return jsonify({'YOUR ANSWER HERE': 'AS A DICTIONARY'})"
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
        # BEGIN SOLUTION PROMPT="return jsonify({'YOUR ANSWER HERE': 'AS A DICTIONARY'})"
        return jsonify(
            {
                "status": "error",
                "message": f"Track image for artist {artist_name} and song title {song_title} not found",
            }
        ), HTTPStatus.NOT_FOUND
        # END SOLUTION

    # BEGIN SOLUTION PROMPT="return jsonify({'YOUR ANSWER HERE': 'AS A DICTIONARY'})"
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
    # TODO docstring
    # TODO starter code markers/prompts
    # TODO tests

    result = {
        "title": "",  # TODO(Abby)
        "image": "",  # TODO(Abby)
        "playlist": [],
    }

    database = db.get_db()
    query = "SELECT * FROM songs"
    rows = database.execute(query).fetchall()
    chosen_songs = sample(
        rows, NUM_SONGS_IN_DAYLIST
    )  # TODO set seed? make seed a parameter?

    for song in chosen_songs:
        result["playlist"].append(
            {
                "title": song["track_name"],
                "artist": song["artist_name"],
                "album": song["album_name"],
                "album_cover": song["album_image_url"],
                "duration": int(song["duration"]),  # TODO do we want to round here?
            }
        )

    return jsonify(result), HTTPStatus.OK
