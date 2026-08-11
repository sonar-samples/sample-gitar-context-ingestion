"""Tests for the demo application's routes."""

from flask.testing import FlaskClient


def test_health_check(client: FlaskClient) -> None:
    """The health endpoint reports that the service is available."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
