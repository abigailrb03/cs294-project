from flask import Blueprint, jsonify, request
from http import HTTPStatus

from . import db

# Create the api Blueprint
bp = Blueprint('api', __name__)

@bp.route("/api/track-image", methods=['GET'])
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
    artist_name = _______
    song_title = _______

    if _______:
        return jsonify({'YOUR ANSWER HERE': 'AS A DICTIONARY'})

    database = db.get_db()
    query = _______
    row = database.execute(query, (artist_name, song_title)).fetchone()

    if _______:
        return jsonify({'YOUR ANSWER HERE': 'AS A DICTIONARY'})

    return jsonify({'YOUR ANSWER HERE': 'AS A DICTIONARY'})
