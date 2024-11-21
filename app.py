# app.py

from flask import Flask, jsonify, request
from models import get_orders_by_manufacturer_and_status, get_order_by_id

app = Flask(__name__)


# API to get all orders given a manufacturerId and status
@app.route('/orders', methods=['GET'])
def get_orders():
    manufacturer_id = request.args.get('manufacturerId', type=int)
    status = request.args.get('status', type=str)

    if manufacturer_id is None or status is None:
        return jsonify({"error": "Missing manufacturerId or status"}), 400

    orders = get_orders_by_manufacturer_and_status(manufacturer_id, status)

    if not orders:
        return jsonify({"message": "No orders found"}), 404

    return jsonify(orders), 200


# API to get a single order by orderId
@app.route('/order/<int:order_id>', methods=['GET'])
def get_single_order(order_id):
    order = get_order_by_id(order_id)

    if not order:
        return jsonify({"message": "Order not found"}), 404

    return jsonify(order), 200


if __name__ == '__main__':
    app.run(debug=True)
