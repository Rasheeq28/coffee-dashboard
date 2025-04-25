import sqlite3
import pandas as pd
import json

# Connect to the SQLite database
conn = sqlite3.connect("sheets_data.db")

# Load the sheet table (assuming it was saved as '201904_sales_reciepts')
table_name = "201904_sales_reciepts"

# Read the table into a DataFrame
df = pd.read_sql_query(f'SELECT * FROM "{table_name}"', conn)

# Count non-null transaction IDs in column A
total_transactions = df["transaction_id"].count()

# Save the total into a JSON file to be used by app.py
result = {"total_transactions": total_transactions}
with open("metrics.json", "w") as f:
    json.dump(result, f)

print(f"✅ Total transactions calculated: {total_transactions}")
conn.close()
