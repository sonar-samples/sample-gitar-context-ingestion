"""HTTP routes for the demo application."""

from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.get("/health")
def health_check():
    """Return the service health state."""
    return jsonify({"status": "ok"})
