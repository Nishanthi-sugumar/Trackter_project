# models.py

from db import get_db_connection


def get_orders_by_manufacturer_and_status(manufacturer_id, status):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    query = """
    SELECT * FROM order_table
    WHERE manufacturer_id = %s AND order_status = %s;
    """

    cursor.execute(query, (manufacturer_id, status))
    orders = cursor.fetchall()

    cursor.close()
    conn.close()

    return orders


def get_order_by_id(order_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    query = """
    SELECT * FROM order_table
    WHERE id = %s;
    """

    cursor.execute(query, (order_id,))
    order = cursor.fetchone()

    cursor.close()
    conn.close()

    return order
