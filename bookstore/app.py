from flask import Flask, abort, jsonify, request

from bookstore import db, orders

app = Flask(__name__)
conn = db.connect()


@app.get("/books")
def books():
    return jsonify(db.list_books(conn))


@app.get("/books/<int:book_id>")
def book(book_id: int):
    found = db.get_book(conn, book_id)
    if found is None:
        abort(404)
    return jsonify(found)


@app.post("/books")
def create_book():
    data = request.get_json()
    book_id = db.add_book(conn, data["title"], data["author"], float(data["price"]))
    return jsonify({"id": book_id}), 201


@app.get("/search")
def search():
    return jsonify(db.search_books(conn, request.args.get("q", "")))


@app.post("/reports/sales")
def sales():
    return jsonify(reports.sales_report(request.get_json()["book_ids"]))


@app.post("/export")
def export():
    reports.export_csv(request.args.get("file", "books.csv"))
    return jsonify({"status": "exported"})

orders.create_orders_table(conn)


@app.post("/orders")
def new_order():
    data = request.get_json()
    order_id = orders.place_order(conn, data["customer"], data["book_id"], data["quantity"])
    orders.charge_customer(data["customer"], data["amount"])
    return jsonify({"id": order_id, "token": orders.order_token(order_id)}), 201


@app.get("/orders/<customer>")
def customer_orders(customer: str):
    return jsonify(orders.orders_for_customer(conn, customer))
