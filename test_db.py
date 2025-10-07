import sqlite3, os
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_NAME")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
INSERT INTO transactions (user_id, household_id, date, amount, type, category, payment_mode, description, tags, linked_bill_id)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "user1", "house1", "2025-10-05", 1000.0, "expense", "groceries", "cash", "Test insert", "food,monthly", None
))

conn.commit()
conn.close()

print("✅ Inserted 1 row")
