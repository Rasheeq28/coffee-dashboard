# # import json
# # import pandas as pd
# # import sqlite3
# #
# # # Connect to the database
# # conn = sqlite3.connect("sheets_data.db")
# # df = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', conn)
# #
# # # Parse date column
# # df['transaction_date'] = pd.to_datetime(df['transaction_date'])
# #
# # # Total transactions
# # transaction_count = int(df['transaction_id'].count())
# #
# # # Calculate daily transaction trend
# # daily_trend = (
# #     df.groupby(df['transaction_date'].dt.date)['transaction_id']
# #     .count()
# #     .reset_index()
# #     .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
# # )
# #
# # # Convert dates to strings for JSON serialization
# # daily_trend['date'] = daily_trend['date'].astype(str)
# #
# # # Create a list of daily transactions
# # daily_transactions = daily_trend.to_dict(orient='records')
# #
# # # Combine into one dictionary
# # metrics = {
# #     "total_transactions": transaction_count,
# #     "daily_transactions": daily_transactions
# # }
# #
# # # Save everything to metrics.json
# # with open("metrics.json", "w") as f:
# #     json.dump(metrics, f, indent=4)
# #
# # # Close connection
# # conn.close()
# import json
# import pandas as pd
# import sqlite3
#
# # Connect to the database
# conn = sqlite3.connect("sheets_data.db")
# df = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', conn)
#
# # Parse date column
# df['transaction_date'] = pd.to_datetime(df['transaction_date'])
#
# # Total transactions
# transaction_count = int(df['transaction_id'].count())
#
# # Daily overall transaction trend
# daily_trend = (
#     df.groupby(df['transaction_date'].dt.date)['transaction_id']
#     .count()
#     .reset_index()
#     .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
# )
# daily_trend['date'] = daily_trend['date'].astype(str)  # Convert date to string
# daily_transactions = daily_trend.to_dict(orient='records')
#
# # Daily transactions per outlet
# per_outlet_trend = (
#     df.groupby([df['transaction_date'].dt.date, 'sales_outlet_id'])['transaction_id']
#     .count()
#     .reset_index()
#     .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
# )
# per_outlet_trend['date'] = per_outlet_trend['date'].astype(str)  # Convert date to string
# outlet_transactions = per_outlet_trend.to_dict(orient='records')
#
# # Save to metrics.json
# metrics = {
#     "total_transactions": transaction_count,
#     "daily_transactions": daily_transactions,
#     "outlet_transactions": outlet_transactions
# }
#
# with open("metrics.json", "w") as f:
#     json.dump(metrics, f, indent=4)
#
# conn.close()


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

# Daily transaction trend
daily_trend = (
    df.groupby(df['transaction_date'].dt.date)['transaction_id']
    .count()
    .reset_index()
    .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
)
daily_trend['date'] = daily_trend['date'].astype(str)
daily_transactions = daily_trend.to_dict(orient='records')

# Store-wise daily transaction trend
outlet_trend = (
    df.groupby([df['transaction_date'].dt.date, 'sales_outlet_id'])['transaction_id']
    .count()
    .reset_index()
    .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'transaction_date'})
)
outlet_trend['transaction_date'] = outlet_trend['transaction_date'].astype(str)
outlet_daily_transactions = outlet_trend.to_dict(orient='records')

# Final metrics
metrics = {
    "total_transactions": transaction_count,
    "daily_transactions": daily_transactions,
    "outlet_daily_transactions": outlet_daily_transactions
}

# Save everything to metrics.json
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

conn.close()
