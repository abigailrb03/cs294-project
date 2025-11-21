from daylist.dao import DataAccessObject, Song


def test_dao(test_db):
    dao = DataAccessObject(test_db)
    songs = dao.get_all_songs()

    assert type(songs) is list

    for i in range(len(songs)):
        assert type(songs[i]) is dict

    assert len(songs) == 100


def test_get_song_by_title_and_artist(test_db):
    dao = DataAccessObject(test_db)
    song_obj = dao.get_song_by_title_and_artist("Genius", "Ravyn Lenae")
    correct_song = Song(
        "Genius",
        "Ravyn Lenae",
        "Bird's Eye",
        "https://i.scdn.co/image/ab67616d0000b273ef985ba96e76a9574cc68a30",
        156,
    )

    assert type(song_obj) is Song
    assert song_obj == correct_song
