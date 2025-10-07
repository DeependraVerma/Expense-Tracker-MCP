from pydantic import BaseModel
import sqlite3 
import os
from typing import Optional, List
from datetime import date
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_NAME")

print(DB_PATH)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        household_id TEXT NOT NULL,
        date TEXT NOT NULL,
        amount REAL NOT NULL,
        type TEXT CHECK(type IN ('expense','income','transfer')) NOT NULL,
        category TEXT,
        payment_mode TEXT,
        description TEXT,
        tags TEXT,
        linked_bill_id TEXT
    );
""")
    conn.commit()
    conn.close()
    print("DB Initiated")
