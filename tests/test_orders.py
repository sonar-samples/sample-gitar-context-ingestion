"""Tests for the order API."""

from flask.testing import FlaskClient


def test_order_lifecycle(client: FlaskClient) -> None:
    """An order can be created, retrieved, and cancelled."""
    create_response = client.post(
        "/orders",
        json={"sku": "SKU-RED-CHAIR", "quantity": 2},
    )

    assert create_response.status_code == 201
    order = create_response.get_json()["order"]
    assert order["sku"] == "SKU-RED-CHAIR"
    assert order["quantity"] == 2

    get_response = client.get(f"/orders/{order['id']}")

    assert get_response.status_code == 200
    assert get_response.get_json() == {"order": order}

    cancel_response = client.delete(f"/orders/{order['id']}")

    assert cancel_response.status_code == 200
    assert cancel_response.get_json() == {"cancelled_order": order}
