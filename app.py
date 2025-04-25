# import streamlit as st
# import pandas as pd
# import sqlite3
#
# # Connect to the SQLite database
# def load_table(table_name):
#     conn = sqlite3.connect("sheets_data.db")
#     df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
#     conn.close()
#     return df
#
# # Get table names from the database
# def get_table_names():
#     conn = sqlite3.connect("sheets_data.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     tables = [row[0] for row in cursor.fetchall()]
#     conn.close()
#     return tables
#
# st.set_page_config(page_title="Google Sheets Dashboard", layout="wide")
# st.title("📊 Google Sheets Dashboard")
#
# # Sidebar for table selection
# st.sidebar.header("Select a Table")
# tables = get_table_names()
# selected_table = st.sidebar.selectbox("Choose a table to view", tables)
#
# # Display data from selected table
# if selected_table:
#     df = load_table(selected_table)
#     st.subheader(f"Table: {selected_table}")
#     st.dataframe(df)
#
#     # Basic summary stats
#     with st.expander("🔍 Summary Statistics"):
#         st.write(df.describe(include='all'))
#
#     # Optional charting if numeric columns exist
#     numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
#     if numeric_cols:
#         st.sidebar.subheader("Chart Options")
#         chart_col = st.sidebar.selectbox("Choose a column to chart", numeric_cols)
#         st.line_chart(df[chart_col])
# dashboard.py
# import streamlit as st
# import json
# import pandas as pd
#
# # Load metrics from analysis
# with open("metrics.json", "r") as f:
#     metrics = json.load(f)
#
# # Show total transactions
# st.markdown(f"### 💰 Total transactions till date: **{metrics['total_transactions']}**")
#
# # Load daily transaction trend into a DataFrame
# daily_df = pd.DataFrame(metrics["daily_transactions"])
#
# # Convert date column to datetime for plotting
# daily_df["date"] = pd.to_datetime(daily_df["date"])
#
# # Show line chart
# st.markdown("### 📈 Daily Transaction Trend")
# st.line_chart(daily_df.set_index("date")["transactions"])
import streamlit as st
import json
import pandas as pd

# Load metrics
with open("metrics.json", "r") as f:
    metrics = json.load(f)

# Show total transactions
st.markdown(f"### 💰 Total transactions till date: **{metrics['total_transactions']}**")

# === Daily Overall Transaction Trend ===
st.markdown("### 📈 Daily Transaction Trend (All Stores Combined)")
daily_df = pd.DataFrame(metrics["daily_transactions"])
daily_df["date"] = pd.to_datetime(daily_df["date"])
st.line_chart(daily_df.set_index("date")["transactions"])

# === Daily Transactions Per Outlet ===
st.markdown("### 🏪 Daily Transactions Per Sales Outlet")
outlet_df = pd.DataFrame(metrics["outlet_transactions"])
outlet_df["date"] = pd.to_datetime(outlet_df["date"])

# Pivot for Streamlit chart: dates as index, outlet IDs as columns
pivot_df = outlet_df.pivot(index="date", columns="sales_outlet_id", values="transactions")
st.line_chart(pivot_df)
