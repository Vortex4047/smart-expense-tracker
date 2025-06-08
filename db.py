import sqlite3

def init_db():
    conn = sqlite3.connect("receipts.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            merchant TEXT,
            category TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_expense(expense):
    conn = sqlite3.connect("receipts.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (date, merchant, category, amount) VALUES (?, ?, ?, ?)",
                (expense["date"], expense["merchant"], expense["category"], expense["amount"]))
    conn.commit()
    conn.close()
