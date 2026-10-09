import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL
);
"""


def connect(path: str = "bookstore.db") -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def add_book(conn: sqlite3.Connection, title: str, author: str, price: float) -> int:
    cur = conn.execute(
        "INSERT INTO books (title, author, price) VALUES (?, ?, ?)", (title, author, price)
    )
    conn.commit()
    return cur.lastrowid


def get_book(conn: sqlite3.Connection, book_id: int) -> dict | None:
    row = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    return dict(row) if row else None


def list_books(conn: sqlite3.Connection) -> list[dict]:
    return [dict(r) for r in conn.execute("SELECT * FROM books ORDER BY title")]


def search_books(conn: sqlite3.Connection, query: str) -> list[dict]:
    sql = f"SELECT * FROM books WHERE title LIKE '%{query}%' OR author LIKE '%{query}%'"
    return [dict(r) for r in conn.execute(sql)]
