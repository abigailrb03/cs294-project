from flask import Flask, render_template
from . import db

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

    return app