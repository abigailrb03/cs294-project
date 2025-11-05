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


@pytest.fixture()
def daylist_playlist_default():
    return [
        {
            "album": "More",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273bcfcf81e7e58a3d60ccadb96",
            "artist": "Carly Rae Jepsen",
            "duration": 204,
            "title": "More",
        },
        {
            "album": "Are You Happy Now?",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273b1cf2470a32927df0619baf8",
            "artist": "Jensen McRae",
            "duration": 194,
            "title": "Adam's Ribs",
        },
        {
            "album": "The Life of a Showgirl",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273d7812467811a7da6e6a44902",
            "artist": "Taylor Swift",
            "duration": 226,
            "title": "The Fate of Ophelia",
        },
        {
            "album": "Lover",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273e787cffec20aa2a396a61647",
            "artist": "Taylor Swift",
            "duration": 190,
            "title": "London Boy",
        },
        {
            "album": "Anyone Can See",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2739c5fce0c1e34f0ed438f8614",
            "artist": "Irene Cara",
            "duration": 221,
            "title": "Thunder in My Heart",
        },
        {
            "album": "American Heart",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27311b6c087ac030b4e396e32c0",
            "artist": "Benson Boone",
            "duration": 172,
            "title": "Young American Heart",
        },
        {
            "album": "Arcane League of Legends: Season 2 Original Soundtrack (Extended Edition)",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273590fc7cd8813dc1789a595e3",
            "artist": "King Princess",
            "duration": 187,
            "title": "Fantastic (Live From Vevo) (from the series Arcane League of Legends)",
        },
        {
            "album": "DON'T GROW UP TOO SOON",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27348e5505dce6c5980e03c10e2",
            "artist": "Nascent",
            "duration": 189,
            "title": "Mangosteen (feat. Sailorr & Biako)",
        },
        {
            "album": "Loveseat",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27338e2ac6ca22c8d1f4d781137",
            "artist": "Still Woozy",
            "duration": 209,
            "title": "Little Things",
        },
        {
            "album": "Beat the Devil",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2737983e66f1fd1321b3255757f",
            "artist": "Maren Morris",
            "duration": 133,
            "title": "Beat the Devil",
        },
        {
            "album": "Greatest Hits",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2732847f04f9de392e290b5a0be",
            "artist": "Blondie",
            "duration": 249,
            "title": "Maria",
        },
        {
            "album": "Survive",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273e6c69a4c4a69e0cdd5105f8e",
            "artist": "Lewis Capaldi",
            "duration": 225,
            "title": "Survive",
        },
        {
            "album": "Sunburn",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2735b26c1b56d89c1416d21db60",
            "artist": "Dominic Fike",
            "duration": 186,
            "title": "Mona Lisa",
        },
        {
            "album": "Stick Season (We'll All Be Here Forever)",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27365a472d8326d4571bf725422",
            "artist": "Noah Kahan",
            "duration": 213,
            "title": "Paul Revere",
        },
        {
            "album": "So Close To What",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27381c06ae612adc448a9636365",
            "artist": "Tate McRae",
            "duration": 183,
            "title": "Siren sounds (bonus)",
        },
        {
            "album": "Alligator Bites Never Heal",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273b245099fe26319344ddf6054",
            "artist": "Doechii",
            "duration": 133,
            "title": "BLOOM",
        },
        {
            "album": "StarX Lover",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2731740a423d4f15d8077f4372c",
            "artist": "Dreamer Isioma",
            "duration": 140,
            "title": "Note To Self",
        },
        {
            "album": "I Don't Know How But They Found Me!",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27397c3583721260e454a20a470",
            "artist": "Jensen McRae",
            "duration": 168,
            "title": "The Rearranger",
        },
        {
            "album": "Blessing In Disguise",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273b3d7f238693b6b2118df7e42",
            "artist": "Stacey Ryan",
            "duration": 208,
            "title": "Nothing Like You",
        },
        {
            "album": "FOUND",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2736cc2073c8aaa88ac51311355",
            "artist": "Matt Hansen",
            "duration": 159,
            "title": "FOUND",
        },
        {
            "album": "In Between Dreams",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27306b42768ebe736eec21336ea",
            "artist": "Jack Johnson",
            "duration": 191,
            "title": "Banana Pancakes",
        },
        {
            "album": "Cosmic",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2733905a6a454b8d6385df2780b",
            "artist": "Celine Wanyi",
            "duration": 151,
            "title": "Cosmic",
        },
        {
            "album": "Sis.",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2737387dc1f6a5db68647337433",
            "artist": "KIRBY",
            "duration": 220,
            "title": "Penny",
        },
        {
            "album": "Heartbeat City",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273473881855ae3ceadb949a625",
            "artist": "The Cars",
            "duration": 234,
            "title": "Drive",
        },
        {
            "album": "Good Luck, Babe!",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27391b4bc7c88d91a42e0f3a8b7",
            "artist": "Chappell Roan",
            "duration": 218,
            "title": "Good Luck, Babe!",
        },
        {
            "album": "Ctrl",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2734c79d5ec52a6d0302f3add25",
            "artist": "SZA",
            "duration": 231,
            "title": "Drew Barrymore",
        },
        {
            "album": "CAPRISONGS",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273a1a30cf13d406a0d5d33ae53",
            "artist": "FKA twigs",
            "duration": 225,
            "title": "oh my love",
        },
        {
            "album": "Loveseat",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27338e2ac6ca22c8d1f4d781137",
            "artist": "Still Woozy",
            "duration": 196,
            "title": "Shit Don't Change",
        },
        {
            "album": "Play",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273d42be8d4bebc9cf111ce98a1",
            "artist": "Ed Sheeran",
            "duration": 221,
            "title": "Old Phone",
        },
        {
            "album": "David Archuleta",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273d6bb9dda881700d6cc2e1255",
            "artist": "David Archuleta",
            "duration": 213,
            "title": "Crush",
        },
        {
            "album": "I Don't Know How But They Found Me!",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27397c3583721260e454a20a470",
            "artist": "Jensen McRae",
            "duration": 142,
            "title": "Mother Wound",
        },
        {
            "album": "If I Can Dream: Elvis Presley with the Royal Philharmonic Orchestra",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2737adaca103b3a58a478bac9f4",
            "artist": "Elvis Presley",
            "duration": 209,
            "title": "Burning Love - with The Royal Philharmonic Orchestra",
        },
        {
            "album": "Short n' Sweet",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273fd8d7a8d96871e791cb1f626",
            "artist": "Sabrina Carpenter",
            "duration": 164,
            "title": "Coincidence",
        },
        {
            "album": "This Wasn't Meant For You Anyway",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2736aa2a180c7b009ca8454ef89",
            "artist": "Lola Young",
            "duration": 214,
            "title": "Walk On By",
        },
        {
            "album": "ITS NOT THAT DEEP",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27347b788346c3b9b1646abfa54",
            "artist": "tg.blk",
            "duration": 110,
            "title": "Motorola Money",
        },
        {
            "album": "DeB\u00cd TiRAR M\u00e1S FOToS",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273bbd45c8d36e0e045ef640411",
            "artist": "Bad Bunny",
            "duration": 237,
            "title": "DtMF",
        },
        {
            "album": "I Don't Know How But They Found Me!",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27397c3583721260e454a20a470",
            "artist": "Jensen McRae",
            "duration": 154,
            "title": "Novelty",
        },
        {
            "album": "More Love - Songs from Little Voice Season One",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273da313ff0ee1a50bee49dfc72",
            "artist": "Sara Bareilles",
            "duration": 264,
            "title": "Little Voice",
        },
        {
            "album": 'NIAMOS! (Chandrilian Club Mix) [From "Andor (Season 2)"]',
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2733b7e74cc00be7c9012a6cfe5",
            "artist": "Nicholas Britell",
            "duration": 254,
            "title": 'NIAMOS! (Chandrilian Club Mix) - From "Andor (Season 2)"',
        },
        {
            "album": "Cry about it! (feat. Ravyn Lenae)",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273b3c0cda77bf57d78e16d4056",
            "artist": "Kali Uchis",
            "duration": 171,
            "title": "Cry about it! (feat. Ravyn Lenae)",
        },
        {
            "album": "Are You Happy Now?",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273b1cf2470a32927df0619baf8",
            "artist": "Jensen McRae",
            "duration": 233,
            "title": "Wolves",
        },
        {
            "album": "I Don't Know How But They Found Me!",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27397c3583721260e454a20a470",
            "artist": "Jensen McRae",
            "duration": 217,
            "title": "I Can Change Him",
        },
        {
            "album": "Bird's Eye",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273ef985ba96e76a9574cc68a30",
            "artist": "Ravyn Lenae",
            "duration": 155,
            "title": "Genius",
        },
        {
            "album": "empathogen",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b2732fde8c7695f5151e26076a4b",
            "artist": "WILLOW",
            "duration": 188,
            "title": "run!",
        },
        {
            "album": "A Time For Us",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273a10884176b5db201bdd1279b",
            "artist": "Mel Torm\u00e9",
            "duration": 238,
            "title": "The Windmills Of Your Mind",
        },
        {
            "album": "The Celestial Suite",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27308b49210c5b49f839428d994",
            "artist": "Pale Jay",
            "duration": 187,
            "title": "Under The Magnolia Tree",
        },
        {
            "album": "MAYHEM",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273b0860cf0a98e09663c82290c",
            "artist": "Lady Gaga",
            "duration": 239,
            "title": "Garden Of Eden",
        },
        {
            "album": "Is This Real?",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27381b1ed74fdb8c1888741bb9d",
            "artist": "The Collarbones",
            "duration": 198,
            "title": "West of London",
        },
        {
            "album": "How To Be A Human Being",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b273ec3d15eab5bd77027abc4b23",
            "artist": "Glass Animals",
            "duration": 271,
            "title": "Agnes",
        },
        {
            "album": "I Don't Know How But They Found Me!",
            "album_cover": "https://i.scdn.co/image/ab67616d0000b27397c3583721260e454a20a470",
            "artist": "Jensen McRae",
            "duration": 218,
            "title": "Massachusetts",
        },
    ]
