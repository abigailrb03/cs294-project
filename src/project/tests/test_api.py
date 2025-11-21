from http import HTTPStatus


def test_track_image_request(client):
    response = client.get(
        "/api/track-image",
        query_string={"artist": "Taylor Swift", "title": "Elizabeth Taylor"},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json["artist"] == "Taylor Swift"
    assert response.json["title"] == "Elizabeth Taylor"
    assert (
        response.json["image_url"]
        == "https://i.scdn.co/image/ab67616d0000b273d7812467811a7da6e6a44902"
    )


def test_track_image_request_missing_artist(client):
    """Test the /api/track-image endpoint fails when a required artist query param is missing."""
    response = client.get(
        "/api/track-image", query_string={"title": "Elizabeth Taylor"}
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json["status"] == "error"
    assert (
        response.json["message"]
        == "Artist name and/or song title not provided as query arguments, both are required"
    )


def test_track_image_request_missing_title(client):
    """Test the /api/track-image endpoint fails when a required title query param is missing."""
    response = client.get("/api/track-image", query_string={"artist": "Taylor Swift"})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json["status"] == "error"
    assert (
        response.json["message"]
        == "Artist name and/or song title not provided as query arguments, both are required"
    )


def test_track_image_request_not_found(client):
    """
    Test the /api/track-image endpoint fails with 404 when the track is
    not found in the database.
    """
    response = client.get(
        "/api/track-image",
        query_string={"artist": "Ed Sheeran", "title": "Thinking Out Loud"},
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json["status"] == "error"
    assert (
        response.json["message"]
        == "Track image for artist Ed Sheeran and song title Thinking Out Loud not found"
    )


def test_daylist_playlist_length(client, daylist_playlist_default):
    """
    Test the /api/daylist endpoint responds with 200 OK
    and a playlist of the correct 50 songs for the default seed.
    """
    response = client.get("/api/daylist")
    assert response.status_code == HTTPStatus.OK

    playlist = response.json["playlist"]
    assert len(playlist) == 50
    assert playlist == daylist_playlist_default


def test_daylist_playlist_diff_seed(client):
    """
    Test the /api/daylist endpoint responds with 200 OK
    and randomly generates a playlist of 50 songs
    that are different when different seeds are provided.
    """
    response_one = client.get("/api/daylist")  # use default seed of 88
    assert response_one.status_code == HTTPStatus.OK
    playlist_one = response_one.json["playlist"]
    assert len(playlist_one) == 50

    response_two = client.get("/api/daylist", query_string={"seed": 42})
    assert response_two.status_code == HTTPStatus.OK
    playlist_two = response_two.json["playlist"]
    assert len(playlist_two) == 50

    assert playlist_one != playlist_two


def test_daylist_playlist_same_seed(client):
    """
    Test the /api/daylist endpoint responds with
    the same random sample of songs when given the same seed.
    """
    response_one = client.get("/api/daylist")  # use default seed of 88
    assert response_one.status_code == HTTPStatus.OK
    playlist_one = response_one.json["playlist"]
    assert len(playlist_one) == 50

    response_two = client.get("/api/daylist")  # use default seed of 88
    assert response_two.status_code == HTTPStatus.OK
    playlist_two = response_two.json["playlist"]
    assert len(playlist_two) == 50

    assert playlist_one == playlist_two


def test_daylist_title_different(client):
    """
    Test that two calls to the /api/daylist endpoint responds with different titles
    """
    response_one = client.get("/api/daylist")
    assert response_one.status_code == HTTPStatus.OK

    response_two = client.get("/api/daylist")
    assert response_two.status_code == HTTPStatus.OK

    assert response_one.json["title"] != response_two.json["title"]


def test_daylist_title_different_many(client):
    """
    Test that 10 calls to the /api/daylist endpoint responds with different titles
    """
    titles = []
    for _ in range(10):
        response = client.get("/api/daylist")
        assert response.status_code == HTTPStatus.OK
        titles.append(response.json["title"])

    assert len(set(titles)) == 10