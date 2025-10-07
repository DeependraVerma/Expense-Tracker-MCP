import random
from fastmcp import FastMCP
import sqlite3
import os
from sqlite_db import init_db
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

DB_PATH  = os.getenv("DB_NAME")

init_db()

mcp = FastMCP(name="Expense Tracker")

@mcp.tool
def add_transaction_tool(user_id, household_id, amount, type, category, payment_mode, description="", tags="", linked_bill_id=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO transactions (user_id, household_id, date, amount, type, category, payment_mode, description, tags, linked_bill_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id,household_id, date, amount, type, category, payment_mode, description, tags, linked_bill_id))
    conn.commit()
    conn.close()
    return {"status":"success", "message":"Transaction Added"}



@mcp.tool
def get_transaction_tool(user_id:str, household_id:str, category:str=None, payment_mode:str =None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = "SELECT * FROM transactions WHERE user_id=? AND household_id=?"
    params = [user_id, household_id]
    if category:
        query +="AND category=?"
        params.append(category)
    if payment_mode:
        query +="AND payment_mode=?"
        params.append(payment_mode)
    cursor.execute(query, tuple(params))
    row = cursor.fetchall()
    conn.close()
    return row

@mcp.tool
def get_summary(household_id, user_id=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = "SELECT * FROM transactions WHERE household_id=?"
    params = [household_id]
    if user_id:
        query +="AND user_id=?"
        params.append(user_id)
    cursor.execute(query, tuple(params))
    rows = cursor.fetchall()
    conn.close()
    return rows



if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0", port=8000)
     