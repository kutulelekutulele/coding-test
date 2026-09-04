import sqlite3
from datetime import datetime

DB_FILE = "receipts.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # biar hasil query bisa diakses kayak dict
    return conn

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            merchant TEXT NOT NULL,
            purchase_date TEXT NOT NULL,
            item_name TEXT NOT NULL,
            price INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_item(merchant, purchase_date, item_name, price):
    conn = get_connection()
    conn.execute(
        "INSERT INTO receipts (merchant, purchase_date, item_name, price, created_at) VALUES (?, ?, ?, ?, ?)",
        (merchant, purchase_date, item_name, price, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

def get_items_by_date(date):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM receipts WHERE purchase_date = ?", (date,)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_total_by_date(date):
    conn = get_connection()
    result = conn.execute(
        "SELECT SUM(price) as total FROM receipts WHERE purchase_date = ?", (date,)
    ).fetchone()
    conn.close()
    return result["total"] or 0

def get_merchants_by_item_and_daterange(item_keyword, start_date, end_date):
    conn = get_connection()
    rows = conn.execute(
        """SELECT DISTINCT merchant, purchase_date FROM receipts
           WHERE item_name LIKE ? AND purchase_date BETWEEN ? AND ?""",
        (f"%{item_keyword}%", start_date, end_date)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]
