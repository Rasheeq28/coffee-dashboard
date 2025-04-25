# # # # import streamlit as st
# # # # import pandas as pd
# # # # import sqlite3
# # # #
# # # # # Connect to the SQLite database
# # # # def load_table(table_name):
# # # #     conn = sqlite3.connect("sheets_data.db")
# # # #     df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
# # # #     conn.close()
# # # #     return df
# # # #
# # # # # Get table names from the database
# # # # def get_table_names():
# # # #     conn = sqlite3.connect("sheets_data.db")
# # # #     cursor = conn.cursor()
# # # #     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# # # #     tables = [row[0] for row in cursor.fetchall()]
# # # #     conn.close()
# # # #     return tables
# # # #
# # # # st.set_page_config(page_title="Google Sheets Dashboard", layout="wide")
# # # # st.title("📊 Google Sheets Dashboard")
# # # #
# # # # # Sidebar for table selection
# # # # st.sidebar.header("Select a Table")
# # # # tables = get_table_names()
# # # # selected_table = st.sidebar.selectbox("Choose a table to view", tables)
# # # #
# # # # # Display data from selected table
# # # # if selected_table:
# # # #     df = load_table(selected_table)
# # # #     st.subheader(f"Table: {selected_table}")
# # # #     st.dataframe(df)
# # # #
# # # #     # Basic summary stats
# # # #     with st.expander("🔍 Summary Statistics"):
# # # #         st.write(df.describe(include='all'))
# # # #
# # # #     # Optional charting if numeric columns exist
# # # #     numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
# # # #     if numeric_cols:
# # # #         st.sidebar.subheader("Chart Options")
# # # #         chart_col = st.sidebar.selectbox("Choose a column to chart", numeric_cols)
# # # #         st.line_chart(df[chart_col])
# # # # dashboard.py
# # # # import streamlit as st
# # # # import json
# # # # import pandas as pd
# # # #
# # # # # Load metrics from analysis
# # # # with open("metrics.json", "r") as f:
# # # #     metrics = json.load(f)
# # # #
# # # # # Show total transactions
# # # # st.markdown(f"### 💰 Total transactions till date: **{metrics['total_transactions']}**")
# # # #
# # # # # Load daily transaction trend into a DataFrame
# # # # daily_df = pd.DataFrame(metrics["daily_transactions"])
# # # #
# # # # # Convert date column to datetime for plotting
# # # # daily_df["date"] = pd.to_datetime(daily_df["date"])
# # # #
# # # # # Show line chart
# # # # st.markdown("### 📈 Daily Transaction Trend")
# # # # st.line_chart(daily_df.set_index("date")["transactions"])
# # # import streamlit as st
# # # import json
# # # import pandas as pd
# # #
# # # # Load metrics
# # # with open("metrics.json", "r") as f:
# # #     metrics = json.load(f)
# # #
# # # # Show total transactions
# # # st.markdown(f"### 💰 Total transactions till date: **{metrics['total_transactions']}**")
# # #
# # # # === Daily Overall Transaction Trend ===
# # # st.markdown("### 📈 Daily Transaction Trend (All Stores Combined)")
# # # daily_df = pd.DataFrame(metrics["daily_transactions"])
# # # daily_df["date"] = pd.to_datetime(daily_df["date"])
# # # st.line_chart(daily_df.set_index("date")["transactions"])
# # #
# # # # === Daily Transactions Per Outlet ===
# # # st.markdown("### 🏪 Daily Transactions Per Sales Outlet")
# # # outlet_df = pd.DataFrame(metrics["outlet_transactions"])
# # # outlet_df["date"] = pd.to_datetime(outlet_df["date"])
# # #
# # # # Pivot for Streamlit chart: dates as index, outlet IDs as columns
# # # pivot_df = outlet_df.pivot(index="date", columns="sales_outlet_id", values="transactions")
# # # st.line_chart(pivot_df)
# #
# #
# # import streamlit as st
# # import json
# # import pandas as pd
# #
# # # Load metrics from analysis
# # with open("metrics.json", "r") as f:
# #     metrics = json.load(f)
# #
# # # Show total transactions
# # st.markdown(f"### 💰 Total transactions till date: **{metrics['total_transactions']}**")
# #
# # # Daily transaction trend
# # daily_df = pd.DataFrame(metrics["daily_transactions"])
# # daily_df["date"] = pd.to_datetime(daily_df["date"])
# # st.markdown("### 📈 Daily Transaction Trend")
# # st.line_chart(daily_df.set_index("date")["transactions"])
# #
# # # Outlet-wise transaction trend
# # outlet_df = pd.DataFrame(metrics["outlet_daily_transactions"])
# # outlet_df["transaction_date"] = pd.to_datetime(outlet_df["transaction_date"])
# #
# # # Pivot for multiseries line chart
# # pivot_df = outlet_df.pivot(index="transaction_date", columns="sales_outlet_id", values="transactions")
# #
# # st.markdown("### 🏪 Store-wise Daily Transaction Trend")
# # st.line_chart(pivot_df)
# #
# import streamlit as st
# import json
# import pandas as pd
#
# # Load metrics
# with open("metrics.json", "r") as f:
#     metrics = json.load(f)
#
# # Show total transactions
# st.markdown(f"### 💰 Total transactions till date: **{metrics['total_transactions']}**")
#
# # Load data
# daily_df = pd.DataFrame(metrics["daily_transactions"])
# outlet_df = pd.DataFrame(metrics["outlet_daily_transactions"])
#
# # Convert to datetime
# daily_df["date"] = pd.to_datetime(daily_df["date"])
# outlet_df["transaction_date"] = pd.to_datetime(outlet_df["transaction_date"])
#
#
# # Filtering options
# filter_option = st.selectbox("📊 Filter transaction trends by:", ["Date", "Store ID"])
#
# if filter_option == "Date":
#     st.markdown("### 📈 Daily Transaction Trend")
#     st.line_chart(daily_df.set_index("date")["transactions"])
#
# elif filter_option == "Store ID":
#     selected_ids = st.multiselect(
#         "🏪 Select Store ID(s):", outlet_df["sales_outlet_id"].unique().tolist()
#     )
#
#     if selected_ids:
#         filtered_df = outlet_df[outlet_df["sales_outlet_id"].isin(selected_ids)]
#         pivot = filtered_df.pivot(index="date", columns="sales_outlet_id", values="transactions")
#         st.markdown("### 🏬 Store-wise Daily Transaction Trend")
#         st.line_chart(pivot)
#     else:
#         st.info("Please select at least one Store ID to view the trend.")



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
# # Sidebar filter options
# filter_option = st.sidebar.radio("Filter by:", ["Date", "Store ID"])
#
# # Load daily transaction trend into a DataFrame
# daily_df = pd.DataFrame(metrics["daily_transactions"])
# daily_df["date"] = pd.to_datetime(daily_df["date"])
#
# # Load outlet-wise daily transactions
# outlet_df = pd.DataFrame(metrics["outlet_daily_transactions"])
# outlet_df["transaction_date"] = pd.to_datetime(outlet_df["transaction_date"])
#
# # Daily Transaction Trend
# if filter_option == "Date":
#     st.markdown("### 📈 Daily Transaction Trend")
#     st.line_chart(daily_df.set_index("date")["transactions"])
#
# # Store-wise Daily Transaction Trend
# elif filter_option == "Store ID":
#     store_ids = outlet_df["sales_outlet_id"].unique()
#     selected_stores = st.multiselect("Select Store IDs to view trends:", store_ids, default=list(store_ids))
#
#     if selected_stores:
#         filtered_outlet_df = outlet_df[outlet_df["sales_outlet_id"].isin(selected_stores)]
#         st.markdown("### 🏬 Store-wise Daily Transaction Trend")
#         chart_data = filtered_outlet_df.pivot_table(index="transaction_date",
#                                                     columns="sales_outlet_id",
#                                                     values="transactions",
#                                                     fill_value=0)
#         st.line_chart(chart_data)
#     else:
#         st.info("Select at least one store to display the trend.")



# import streamlit as st
# import json
# import pandas as pd
#
# # Load metrics from analysis
# with open("metrics.json", "r") as f:
#     metrics = json.load(f)
#
# # Sidebar for filtering mode
# st.sidebar.title("Transactions")
# filter_mode = st.sidebar.radio("Filter by:", ["Date", "Store ID"])
#
# # Show total transactions
# st.markdown(f"### 💰 Total transactions till date: **{metrics['total_transactions']}**")
#
# # Load daily transaction trend
# daily_df = pd.DataFrame(metrics["daily_transactions"])
# daily_df["date"] = pd.to_datetime(daily_df["date"])
#
# # Load outlet-wise daily transaction trend
# outlet_df = pd.DataFrame(metrics["outlet_daily_transactions"])
# outlet_df["date"] = pd.to_datetime(outlet_df["date"])
#
# # Show chart based on filter mode
# if filter_mode == "Date":
#     st.markdown("### 📅 Daily Transaction Trend")
#     st.line_chart(daily_df.set_index("date")["transactions"])
#
# elif filter_mode == "Store ID":
#     st.markdown("### 🏪 Store-wise Daily Transaction Trend")
#
#     # Let user select store(s) to compare
#     available_stores = sorted(outlet_df["sales_outlet_id"].unique())
#     selected_stores = st.multiselect("Select Store ID(s)", available_stores, default=available_stores[:1])
#
#     if selected_stores:
#         filtered_df = outlet_df[outlet_df["sales_outlet_id"].isin(selected_stores)]
#         pivot_df = filtered_df.pivot_table(
#             index="date",
#             columns="sales_outlet_id",
#             values="transactions",
#             aggfunc="sum"
#         ).fillna(0)
#
#         st.line_chart(pivot_df)
#     else:
#         st.info("Please select at least one store to view the trend.")


import streamlit as st
import json
import pandas as pd

# Load metrics from analysis
with open("metrics.json", "r") as f:
    metrics = json.load(f)

# --- Sidebar Filter ---
st.sidebar.title("📊 Transactions")
filter_option = st.sidebar.radio("Filter by:", ["Date", "Store ID"])

# --- Show total transactions ---
st.markdown(f"### 💰 Total transactions till date: **{metrics['total_transactions']}**")

# --- Daily Transactions Chart ---
if filter_option == "Date":
    daily_df = pd.DataFrame(metrics["daily_transactions"])
    daily_df["date"] = pd.to_datetime(daily_df["date"])

    st.markdown("### 📅 Daily Transaction Trend")
    st.line_chart(daily_df.set_index("date")["transactions"])

# --- Store-wise Transaction Chart ---
elif filter_option == "Store ID":
    outlet_df = pd.DataFrame(metrics["outlet_daily_transactions"])

    # Fix: Rename if needed
    if 'transaction_date' in outlet_df.columns:
        outlet_df = outlet_df.rename(columns={'transaction_date': 'date'})

    outlet_df["date"] = pd.to_datetime(outlet_df["date"])

    st.markdown("### 🏬 Store-wise Daily Transaction Trend")

    # Pivot data to get one line per store
    pivot_df = outlet_df.pivot_table(index="date", columns="sales_outlet_id", values="transactions", fill_value=0)

    st.line_chart(pivot_df)
