import json
import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect("sheets_data.db")
df = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', conn)

# Parse date column
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Total transactions
transaction_count = int(df['transaction_id'].count())

# Calculate daily transaction trend
daily_trend = (
    df.groupby(df['transaction_date'].dt.date)['transaction_id']
    .count()
    .reset_index()
    .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
)

# Convert dates to strings for JSON serialization
daily_trend['date'] = daily_trend['date'].astype(str)

# Create a list of daily transactions
daily_transactions = daily_trend.to_dict(orient='records')

# Combine into one dictionary
metrics = {
    "total_transactions": transaction_count,
    "daily_transactions": daily_transactions
}

# Save everything to metrics.json
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

# Close connection
conn.close()
