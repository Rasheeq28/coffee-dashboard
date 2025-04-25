import json
import pandas as pd
import sqlite3

# Connect and calculate transaction count
conn = sqlite3.connect("sheets_data.db")
df = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', conn)
transaction_count = df['transaction_id'].count()
conn.close()

# Convert to native int
transaction_count = int(transaction_count)

# Save to metrics.json
with open("metrics.json", "w") as f:
    json.dump({"total_transactions": transaction_count}, f)
