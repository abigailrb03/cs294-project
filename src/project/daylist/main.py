from flask import Blueprint, render_template
from . import db

# Create the main Blueprint
bp = Blueprint("main", __name__)


@bp.route("/")
def run():
    return render_template("app.html", person="CS88C student")


@bp.route("/songs")
def show_songs():
    database = db.get_db()
    songs = database.execute(
        "SELECT track_name, artist_name, album_image_url FROM songs"
    ).fetchall()
    return render_template("songs.html", songs=songs)
