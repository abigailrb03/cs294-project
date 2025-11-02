from http import HTTPStatus


def test_homepage(client):
    """Test the basic homepage route."""
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    # Check that the default person variable is rendered
    assert b"CS88C student" in response.data
