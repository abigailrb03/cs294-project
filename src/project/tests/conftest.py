import pytest
import sqlite3

from daylist import create_app, db


@pytest.fixture()
def app():
    app = create_app(
        {
            "TESTING": True,
            "DATABASE": ":memory:",  # use lightweight in-memory sqlite db for testing purposes
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def test_db(app):
    with app.app_context():
        conn = sqlite3.connect(":memory:")

        # Inject the test db connection into the app context for use by routes (see db.py:get_db function)
        app.test_db = conn

        # Initialize the schema
        db.init_db()

        yield conn

        # Clean up
        conn.close()
        del app.test_db  # Remove the attribute


@pytest.fixture()
def client(app, test_db):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
