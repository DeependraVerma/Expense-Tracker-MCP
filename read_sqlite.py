import sqlite3

# Path to your DB
db_path = r"D:\MCP\basic_mcp\home_expenses.db"

# Connect to DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in DB:", tables)

# 2. Read contents of each table
for table in tables:
    table_name = table[0]
    print(f"\n--- Data from {table_name} ---")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Print column names
    col_names = [description[0] for description in cursor.description]
    print("Columns:", col_names)

    # Print rows
    for row in rows:
        print(row)

conn.close()
