from flask import Blueprint, jsonify, request
from http import HTTPStatus

from . import db

# Create the api Blueprint
bp = Blueprint('api', __name__)

@bp.route("/api/track-image", methods=['GET'])
def track_image():
    artist_name = request.args.get("artist", default=None)
    song_title = request.args.get("title", default=None)

    if artist_name is None or song_title is None:
        return jsonify({
            "status": "error",
            "message": "Artist name and/or song title not provided as query arguments, both are required",
        }), HTTPStatus.BAD_REQUEST

    database = db.get_db()
    row = database.execute(
        """
        SELECT album_image_url
        FROM songs
        WHERE artist_name = ? AND track_name = ?
        """,
        (artist_name, song_title)
    ).fetchone()

    if row is None:
        return jsonify({
            "status": "error",
            "message": f"Track image for artist {artist_name} and song title {song_title} not found",
        }), HTTPStatus.NOT_FOUND

    return jsonify({
        "artist": artist_name,
        "title": song_title,
        "image_url": row["album_image_url"],
    }), HTTPStatus.OK
