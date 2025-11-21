from daylist.DAO import DatabaseAccessObject, Song
from daylist import create_app

def test_dao():
    app = create_app()
    with app.app_context():
        dao = DatabaseAccessObject()
        songs = dao.get_all_songs()

        assert isinstance(songs, list)
        assert isinstance(songs[0], dict)

def test_get_song_by_title_and_artist():
    app = create_app()
    with app.app_context():
        dao = DatabaseAccessObject()
        song_obj = dao.get_song_by_title_and_artist('Ravyn Lenae', 'Love Me Not')
        correct_song = Song('Love Me Not', 'Ravyn Lenae', 'Bird\'s Eye', 'https://i.scdn.co/image/ab67616d0000b273ef985ba96e76a9574cc68a30', 156)

        assert isinstance(song_obj, Song)
        assert song_obj == correct_song
