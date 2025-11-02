from flask import Flask
import os

from . import db, main, api


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE="instance/songs.db",
    )

    # Apply test config if provided (this will overwrite defaults like DATABASE)
    if test_config is not None:
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    with app.app_context():
        db.init_db()

    # Register Blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(api.bp)

    return app
