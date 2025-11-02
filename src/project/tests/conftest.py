import pytest
import sqlite3

# TODO need to figure out starter code compilation so that it imports flask_app_starter
# or so that students' apps also are called flask_app
from flask_app import create_app

@pytest.fixture()
def app():
    app = create_app({
        "TESTING": True,
        "DATABASE": ":memory:", # use lightweight in-memory sqlite db for testing purposes
    })

    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def test_db(app):
    with app.app_context():
        conn = sqlite3.connect(':memory:')

        # Inject the test db connection into the app context for use by routes (see db.py:get_db function)
        app.test_db = conn

        # Initialize the schema
        with app.open_resource("schema.sql") as f:
             conn.executescript(f.read().decode("utf8"))

        # Seed database
        conn.execute(
            "INSERT INTO songs (song_link, song_id, track_name, artist_name, album_image_url) VALUES (?, ?, ?, ?, ?)",
            ("https://open.spotify.com/track/1jgTiNob5cVyXeJ3WgX5bL?si=ab68100aa0b745a7", "1jgTiNob5cVyXeJ3WgX5bL", "Elizabeth Taylor", "Taylor Swift", "https://i.scdn.co/image/ab67616d0000b273d7812467811a7da6e6a44902")
        )
        conn.commit()

        yield conn

        # Clean up
        conn.close()
        del app.test_db # Remove the attribute

@pytest.fixture()
def client(app, test_db):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
