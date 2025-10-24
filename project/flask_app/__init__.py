from flask import Flask, render_template, jsonify, request
from . import db
from http import HTTPStatus

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    db.init_app(app)

    app.config["DATABASE"] = "instance/songs.db"

    with app.app_context():
        db.init_db()

    @app.route("/")
    def run():
        return render_template('app.html', person="CS88C student")

    @app.route("/songs")
    def show_songs():
        database = db.get_db()
        songs = database.execute(
            "SELECT track_name, artist_name, album_image_url FROM songs"
        ).fetchall()
        return render_template("songs.html", songs=songs)

    @app.route("/api/track-image", methods=['GET'])
    def track_image():
        artist_name = request.args.get("artist", default=None)
        song_title = request.args.get("title", default=None)

        if artist_name is None or song_title is None:
            return jsonify({
                "status": "error",
                "message": "Artist name and/or song title not provided as query arguments, both are required",
            }), HTTPStatus.BAD_REQUEST

        database = db.get_db()
        # TODO: an opportunity to talk about sql injection?
        image_url = database.execute(
            """
            SELECT album_image_url
            FROM songs
            WHERE artist_name = ? AND track_name = ?
            """,
            (artist_name, song_title)
        ).fetchone()

        if image_url is None:
            return jsonify({
                "status": "error",
                "message": f"Track image for artist {artist_name} and song title {song_title} not found",
            }), HTTPStatus.NOT_FOUND

        return jsonify({
            "artist": artist_name,
            "title": song_title,
            "image_url": image_url["album_image_url"],
        }), HTTPStatus.OK

    return app
