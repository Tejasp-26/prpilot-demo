from flask import Flask, abort, jsonify, request

from bookstore import db, reports

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
