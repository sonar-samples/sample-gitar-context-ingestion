"""Application factory for the Gitar context ingestion demo."""

from flask import Flask

from app.orders import orders_api
from app.routes import api


def create_app() -> Flask:
    """Create and configure the Flask application."""
    application = Flask(__name__)
    application.register_blueprint(api)
    application.register_blueprint(orders_api)
    return application
