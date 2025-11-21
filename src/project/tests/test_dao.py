from daylist.dao import Song


def test_get_all_songs(dao):
    songs = dao.get_all_songs()

    assert type(songs) is list

    for i in range(len(songs)):
        assert type(songs[i]) is dict
        assert "title" in songs[i]
        assert "artist" in songs[i]
        assert "album" in songs[i]
        assert "album_cover" in songs[i]
        assert "duration" in songs[i]

    assert len(songs) == 100


def test_get_song_by_title_and_artist_genius(dao):
    actual_song = dao.get_song_by_title_and_artist("Genius", "Ravyn Lenae")
    expected_song = Song(
        "Genius",
        "Ravyn Lenae",
        "Bird's Eye",
        "https://i.scdn.co/image/ab67616d0000b273ef985ba96e76a9574cc68a30",
        156,
    )
    assert type(actual_song) is Song
    assert actual_song == expected_song


def test_get_song_by_title_and_artist_golden(dao):
    actual_song = dao.get_song_by_title_and_artist("Golden", "HUNTR/X")
    expected_song = Song(
        "Golden",
        "HUNTR/X",
        "KPop Demon Hunters (Soundtrack from the Netflix Film)",
        "https://i.scdn.co/image/ab67616d0000b2734dcb6c5df15cf74596ab25a4",
        195,
    )
    assert type(actual_song) is Song
    assert actual_song == expected_song
