from daylist.DAO import DatabaseAccessObject, Song
from daylist import create_app

def test_dao():
    app = create_app()
    with app.app_context():
        dao = DatabaseAccessObject()
        songs = dao.get_all_songs()

        assert isinstance(songs, list)
        assert isinstance(songs[0], dict)
