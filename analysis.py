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

#
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
# # Daily transaction trend
# daily_trend = (
#     df.groupby(df['transaction_date'].dt.date)['transaction_id']
#     .count()
#     .reset_index()
#     .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
# )
# daily_trend['date'] = daily_trend['date'].astype(str)
# daily_transactions = daily_trend.to_dict(orient='records')
#
# # Store-wise daily transaction trend
# outlet_trend = (
#     df.groupby([df['transaction_date'].dt.date, 'sales_outlet_id'])['transaction_id']
#     .count()
#     .reset_index()
#     .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'transaction_date'})
# )
# outlet_trend['transaction_date'] = outlet_trend['transaction_date'].astype(str)
# outlet_daily_transactions = outlet_trend.to_dict(orient='records')
#
# # Final metrics
# metrics = {
#     "total_transactions": transaction_count,
#     "daily_transactions": daily_transactions,
#     "outlet_daily_transactions": outlet_daily_transactions
# }
#
# # Save everything to metrics.json
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

# Calculate sales
df['sales'] = df['quantity'] * df['unit_price']

# Total transactions
transaction_count = int(df['transaction_id'].count())

# Total sales
total_sales = float(df['sales'].sum())

# Daily transaction trend
daily_trend = (
    df.groupby(df['transaction_date'].dt.date)['transaction_id']
    .count()
    .reset_index()
)
daily_trend.columns = ['date', 'transactions']
daily_trend['date'] = daily_trend['date'].astype(str)
daily_transactions = daily_trend.to_dict(orient='records')

# Store-wise daily transaction trend
outlet_trend = (
    df.groupby([df['transaction_date'].dt.date, 'sales_outlet_id'])['transaction_id']
    .count()
    .reset_index()
)
outlet_trend.columns = ['transaction_date', 'store_id', 'transactions']
outlet_trend['transaction_date'] = outlet_trend['transaction_date'].astype(str)
outlet_daily_transactions = outlet_trend.to_dict(orient='records')

# Daily sales trend
daily_sales_df = (
    df.groupby(df['transaction_date'].dt.date)['sales']
    .sum()
    .reset_index()
)
daily_sales_df.columns = ['date', 'sales']
daily_sales_df['date'] = daily_sales_df['date'].astype(str)
daily_sales = daily_sales_df.to_dict(orient='records')

# Store-wise sales
store_sales_df = (
    df.groupby('sales_outlet_id')['sales']
    .sum()
    .reset_index()
)
store_sales_df.columns = ['store_id', 'sales']
store_sales = store_sales_df.to_dict(orient='records')

# Final metrics
metrics = {
    "total_transactions": transaction_count,
    "daily_transactions": daily_transactions,
    "outlet_daily_transactions": outlet_daily_transactions,
    "total_sales": total_sales,
    "daily_sales": daily_sales,
    "store_sales": store_sales
}

# Save everything to metrics.json
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

conn.close()
