"""Order creation, lookup, and cancellation endpoints."""

from itertools import count

from flask import Blueprint, jsonify, request

orders_api = Blueprint("orders_api", __name__)

_orders: dict[int, dict[str, int | str]] = {}
_order_ids = count(1)


@orders_api.post("/orders")
def create_order():
    payload = request.get_json()
    order = {
        "id": next(_order_ids),
        "sku": payload["sku"],
        "quantity": int(payload["quantity"]),
    }
    _orders[order["id"]] = order
    return jsonify({"order": order}), 201


@orders_api.get("/orders/<int:order_id>")
def get_order(order_id: int):
    return jsonify({"order": _orders.get(order_id)})


@orders_api.delete("/orders/<int:order_id>")
def cancel_order(order_id: int):
    order = _orders.pop(order_id)
    return jsonify({"cancelled_order": order})
