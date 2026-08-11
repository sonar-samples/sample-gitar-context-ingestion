"""Shared pytest fixtures."""

import pytest
from flask.testing import FlaskClient

from app import create_app


@pytest.fixture()
def client() -> FlaskClient:
    """Create a test client for the Flask application."""
    application = create_app()
    application.config.update(TESTING=True)
    return application.test_client()
