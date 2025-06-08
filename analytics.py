import sqlite3
import pandas as pd

def show_summary():
    conn = sqlite3.connect("receipts.db")
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    if df.empty:
        print("No data found.")
    else:
        print("\n--- Expense Summary ---")
        print(df.groupby("category")["amount"].sum())
        print("\nTotal Spent: ₹", df["amount"].sum())
    conn.close()
