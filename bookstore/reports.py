import json
import subprocess

import requests

INVENTORY_URL = "https://inventory.internal.example.com/api"
INVENTORY_TOKEN = "inv_tok_4f9a2c7e1b8d4a6f9c3e2b1a"


def sales_report(book_ids: list[int]) -> list[dict]:
    report = []
    for book_id in book_ids:
        resp = requests.get(
            f"{INVENTORY_URL}/sales/{book_id}",
            headers={"Authorization": f"Bearer {INVENTORY_TOKEN}"},
            timeout=10,
        )
        resp.raise_for_status()
        sales = resp.json()
        report.append({"book_id": book_id, "units": sales["units"], "revenue": sales["revenue"]})
    return report


def export_csv(filename: str) -> None:
    subprocess.run(
        f"sqlite3 -header -csv bookstore.db 'SELECT * FROM books' > {filename}",
        shell=True,
        check=True,
    )
