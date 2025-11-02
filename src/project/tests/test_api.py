from http import HTTPStatus

def test_track_image_request(client):
    response = client.get(f"/api/track-image", query_string={"artist": "Taylor Swift", "title": "Elizabeth Taylor"})
    assert response.status_code == HTTPStatus.OK
    assert response.json["artist"] == "Taylor Swift"
    assert response.json["title"] == "Elizabeth Taylor"
    assert response.json["image_url"] == "https://i.scdn.co/image/ab67616d0000b273d7812467811a7da6e6a44902"

def test_track_image_request_missing_artist(client):
    """Test the /api/track-image endpoint fails when a required artist query param is missing."""
    response = client.get("/api/track-image", query_string={"title": "Elizabeth Taylor"})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json["status"] == "error"
    assert response.json["message"] == "Artist name and/or song title not provided as query arguments, both are required"

def test_track_image_request_missing_title(client):
    """Test the /api/track-image endpoint fails when a required title query param is missing."""
    response = client.get("/api/track-image", query_string={"artist": "Taylor Swift"})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json["status"] == "error"
    assert response.json["message"] == "Artist name and/or song title not provided as query arguments, both are required"

def test_track_image_request_not_found(client):
    """
    Test the /api/track-image endpoint fails with 404 when the track is
    not found in the database.
    """
    response = client.get("/api/track-image", query_string={"artist": "Ed Sheeran", "title": "Thinking Out Loud"})
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json["status"] == "error"
    assert response.json["message"] == "Track image for artist Ed Sheeran and song title Thinking Out Loud not found"
