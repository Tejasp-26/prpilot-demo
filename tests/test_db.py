from bookstore import db


def test_add_and_get_book():
    conn = db.connect(":memory:")
    book_id = db.add_book(conn, "Dune", "Frank Herbert", 9.99)
    assert db.get_book(conn, book_id)["title"] == "Dune"


def test_list_books_sorted():
    conn = db.connect(":memory:")
    db.add_book(conn, "B", "x", 1)
    db.add_book(conn, "A", "y", 2)
    assert [b["title"] for b in db.list_books(conn)] == ["A", "B"]


def test_search_books():
    conn = db.connect(":memory:")
    db.add_book(conn, "Dune", "Frank Herbert", 9.99)
    assert len(db.search_books(conn, "dune")) == 1
