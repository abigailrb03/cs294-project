import sqlite3
from flask import current_app, g
import click
import csv
import os

def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:
        # Use test db fixture if it exists
        if hasattr(current_app, "test_db"):
            g.db = current_app.test_db
        else:
            g.db = sqlite3.connect(
                current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
            )

        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))
    #for now, loading here so there's less overhead
    load_songs_to_db()

def load_songs_to_db():
    db = get_db()
    data_path = os.path.join(os.path.dirname(__file__), "data", "songs_metadata.csv")
    with open(data_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            db.execute(
                "INSERT INTO songs (song_link, song_id, track_name, artist_name, album_image_url) VALUES (?, ?, ?, ?, ?)",
                (row["song_link"], row["song_id"], row["track_name"], row["artist_name"], row["album_image_url"])
            )
    db.commit()


@click.command("init-db")
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

@click.command("load-songs")
def load_songs_command():
    """Load songs from CSV into the database."""
    load_songs_to_db()
    click.echo("Loaded songs from CSV into the database.")

def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(load_songs_command)