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


# import streamlit as st
# import json
# import pandas as pd
#
# # Load metrics from analysis
# with open("metrics.json", "r") as f:
#     metrics = json.load(f)
#
# # --- Sidebar Filter ---
# st.sidebar.title("📊 Transactions")
# filter_option = st.sidebar.radio("Filter by:", ["Date", "Store ID"])
#
# # --- Show total transactions ---
# st.markdown(f"### 💰 Total transactions till date: **{metrics['total_transactions']}**")
#
# # --- Daily Transactions Chart ---
# if filter_option == "Date":
#     daily_df = pd.DataFrame(metrics["daily_transactions"])
#     daily_df["date"] = pd.to_datetime(daily_df["date"])
#
#     st.markdown("### 📅 Daily Transaction Trend")
#     st.line_chart(daily_df.set_index("date")["transactions"])
#
# # --- Store-wise Transaction Chart ---
# elif filter_option == "Store ID":
#     outlet_df = pd.DataFrame(metrics["outlet_daily_transactions"])
#
#     # Fix: Rename if needed
#     if 'transaction_date' in outlet_df.columns:
#         outlet_df = outlet_df.rename(columns={'transaction_date': 'date'})
#
#     outlet_df["date"] = pd.to_datetime(outlet_df["date"])
#
#     st.markdown("### 🏬 Store-wise Daily Transaction Trend")
#
#     # Pivot data to get one line per store
#     pivot_df = outlet_df.pivot_table(index="date", columns="sales_outlet_id", values="transactions", fill_value=0)
#
#     st.line_chart(pivot_df)

#
# import streamlit as st
# import pandas as pd
# import json
# import sqlite3
# from datetime import datetime
# import plotly.express as px
#
# conn = sqlite3.connect("sheets_data.db")
# df_raw = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', conn)
#
# # Parse dates for filtering and plotting
# df_raw['transaction_date'] = pd.to_datetime(df_raw['transaction_date'])
# # Load precomputed metrics from metrics.json
# with open("metrics.json", "r") as f:
#     metrics = json.load(f)
#
# # Convert to DataFrames
# daily_transactions_df = pd.DataFrame(metrics["daily_transactions"])
# outlet_transactions_df = pd.DataFrame(metrics["outlet_daily_transactions"])
# daily_sales_df = pd.DataFrame(metrics["daily_sales"])
# store_sales_df = pd.DataFrame(metrics["store_sales"])
#
# # Ensure date columns are datetime
# daily_transactions_df["date"] = pd.to_datetime(daily_transactions_df["date"])
# outlet_transactions_df["transaction_date"] = pd.to_datetime(outlet_transactions_df["transaction_date"])
# daily_sales_df["date"] = pd.to_datetime(daily_sales_df["date"])
#
# # Get date range and store list
# min_date = daily_sales_df["date"].min().date()
# max_date = daily_sales_df["date"].max().date()
# store_ids = store_sales_df["store_id"].unique().tolist()
#
# # UI
# st.title("📊 Sales & Transactions Dashboard")
#
# tab1, tab2 = st.tabs(["🧾 Transactions", "💰 Sales"])
#
# # -------------------- TRANSACTIONS TAB --------------------
# with tab1:
#     st.subheader("Transaction Overview")
#     st.metric("Total Transactions", metrics["total_transactions"])
#
#     st.subheader("Daily Transaction Trend")
#     st.line_chart(daily_transactions_df.set_index("date")["transactions"])
#
#     st.subheader("📍 Store-wise Daily Transactions")
#
#     # Get unique store IDs
#     store_options_txn = df_raw['sales_outlet_id'].unique().tolist()
#
#     # Dropdown to select a store
#     selected_store_txn = st.selectbox("Select a store for transaction trend", ["All"] + store_options_txn)
#
#     # Group and prepare transaction trend
#     transactions_by_store = (
#         df_raw.groupby([df_raw['transaction_date'].dt.date, 'sales_outlet_id'])['transaction_id']
#         .count()
#         .reset_index()
#         .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
#     )
#
#     # Filter based on store selection
#     if selected_store_txn != "All":
#         transactions_by_store = transactions_by_store[transactions_by_store['sales_outlet_id'] == selected_store_txn]
#
#     # Pivot for plotting if needed (not mandatory with altair, but optional if you'd like multi-line per store)
#     # Plot line chart
#     fig = px.line(transactions_by_store, x="date", y="transactions",
#                   color="sales_outlet_id" if selected_store_txn == "All" else None,
#                   title=f"Store-wise Daily Transactions for {selected_store_txn}" if selected_store_txn != "All" else "Store-wise Daily Transactions")
#
#     st.plotly_chart(fig, use_container_width=True)
#
# # -------------------- SALES TAB --------------------
# with tab2:
#     st.subheader("Sales Overview")
#     st.metric("Total Sales", f"${metrics['total_sales']:,.2f}")
#
#     # Filters
#     with st.sidebar:
#         st.header("💡 Sales Filters")
#         selected_store = st.selectbox("Store ID", options=["All"] + store_ids)
#         selected_range = st.date_input("Date Range", [min_date, max_date])
#
#     # Load full transaction data for accurate filtering
#     df_raw = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', sqlite3.connect("sheets_data.db"))
#     df_raw['transaction_date'] = pd.to_datetime(df_raw['transaction_date'])
#     df_raw['sales'] = df_raw['quantity'] * df_raw['unit_price']
#
#     # Apply filters to raw data
#     mask = (df_raw['transaction_date'].dt.date >= selected_range[0]) & \
#            (df_raw['transaction_date'].dt.date <= selected_range[1])
#
#     if selected_store != "All":
#         mask &= (df_raw['sales_outlet_id'] == selected_store)
#
#     filtered = df_raw[mask]
#
#     # Daily sales for filtered data
#     daily_filtered_sales = (
#         filtered.groupby(filtered['transaction_date'].dt.date)['sales']
#         .sum()
#         .reset_index()
#     )
#     daily_filtered_sales.columns = ['date', 'sales']
#     daily_filtered_sales['date'] = pd.to_datetime(daily_filtered_sales['date'])
#
#     st.subheader(f"Daily Sales Trend - store {selected_store}")
#     st.line_chart(daily_filtered_sales.set_index("date")["sales"])
#
#     if selected_store == "All":
#         st.subheader("Store-wise Total Sales")
#         st.bar_chart(store_sales_df.set_index("store_id")["sales"])



# sales works
# import streamlit as st
# import pandas as pd
# import json
# import sqlite3
# from datetime import datetime
# import plotly.express as px
#
# conn = sqlite3.connect("sheets_data.db")
# df_raw = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', conn)
#
# # Parse dates for filtering and plotting
# df_raw['transaction_date'] = pd.to_datetime(df_raw['transaction_date'])
# # Load precomputed metrics from metrics.json
# with open("metrics.json", "r") as f:
#     metrics = json.load(f)
#
# # Convert to DataFrames
# daily_transactions_df = pd.DataFrame(metrics["daily_transactions"])
# outlet_transactions_df = pd.DataFrame(metrics["outlet_daily_transactions"])
# daily_sales_df = pd.DataFrame(metrics["daily_sales"])
# store_sales_df = pd.DataFrame(metrics["store_sales"])
#
# # Ensure date columns are datetime
# daily_transactions_df["date"] = pd.to_datetime(daily_transactions_df["date"])
# outlet_transactions_df["transaction_date"] = pd.to_datetime(outlet_transactions_df["transaction_date"])
# daily_sales_df["date"] = pd.to_datetime(daily_sales_df["date"])
#
# # Get date range and store list
# min_date = daily_sales_df["date"].min().date()
# max_date = daily_sales_df["date"].max().date()
# store_ids = store_sales_df["store_id"].unique().tolist()
#
# # UI
# st.title("📊 Sales & Transactions Dashboard")
#
# tab1, tab2 = st.tabs(["🧾 Transactions", "💰 Sales"])
#
# # -------------------- TRANSACTIONS TAB --------------------
# with tab1:
#     st.subheader("Transaction Overview")
#     st.metric("Total Transactions", metrics["total_transactions"])
#
#     st.subheader("Daily Transaction Trend")
#     st.line_chart(daily_transactions_df.set_index("date")["transactions"])
#
#     st.subheader("📍 Store-wise Daily Transactions")
#
#     # Get unique store IDs
#     store_options_txn = df_raw['sales_outlet_id'].unique().tolist()
#
#     # Dropdown to select a store
#     selected_store_txn = st.selectbox("Select a store for transaction trend", ["All"] + store_options_txn)
#
#     # Group and prepare transaction trend
#     transactions_by_store = (
#         df_raw.groupby([df_raw['transaction_date'].dt.date, 'sales_outlet_id'])['transaction_id']
#         .count()
#         .reset_index()
#         .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
#     )
#
#     # Filter based on store selection
#     if selected_store_txn != "All":
#         transactions_by_store = transactions_by_store[transactions_by_store['sales_outlet_id'] == selected_store_txn]
#
#     # Plot line chart
#     fig = px.line(transactions_by_store, x="date", y="transactions",
#                   color="sales_outlet_id" if selected_store_txn == "All" else None,
#                   title=f"Store-wise Daily Transactions for {selected_store_txn}" if selected_store_txn != "All" else "Store-wise Daily Transactions")
#
#     st.plotly_chart(fig, use_container_width=True)
#
# # -------------------- SALES TAB --------------------
# with tab2:
#     st.subheader("Sales Overview")
#
#     # Filters
#     with st.sidebar:
#         st.header("💡 Sales Filters")
#         selected_store = st.selectbox("Store ID", options=["All"] + store_ids)
#         selected_range = st.date_input("Date Range", [min_date, max_date])
#
#     # Load full transaction data for accurate filtering
#     df_raw = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', sqlite3.connect("sheets_data.db"))
#     df_raw['transaction_date'] = pd.to_datetime(df_raw['transaction_date'])
#     df_raw['sales'] = df_raw['quantity'] * df_raw['unit_price']
#
#     # Apply filters to raw data
#     mask = (df_raw['transaction_date'].dt.date >= selected_range[0]) & \
#            (df_raw['transaction_date'].dt.date <= selected_range[1])
#
#     if selected_store != "All":
#         mask &= (df_raw['sales_outlet_id'] == selected_store)
#
#     filtered = df_raw[mask]
#
#     # Total filtered sales
#     total_filtered_sales = filtered['sales'].sum()
#     st.metric("Filtered Total Sales", f"${total_filtered_sales:,.2f}")
#
#     # Daily sales for filtered data
#     daily_filtered_sales = (
#         filtered.groupby(filtered['transaction_date'].dt.date)['sales']
#         .sum()
#         .reset_index()
#     )
#     daily_filtered_sales.columns = ['date', 'sales']
#     daily_filtered_sales['date'] = pd.to_datetime(daily_filtered_sales['date'])
#
#     st.subheader(f"Daily Sales Trend - store {selected_store}")
#     st.line_chart(daily_filtered_sales.set_index("date")["sales"])
#
#     if selected_store == "All":
#         st.subheader("Store-wise Total Sales")
#         st.bar_chart(store_sales_df.set_index("store_id")["sales"])



##perfect filters for sales amd transactions
# import streamlit as st
# import pandas as pd
# import json
# import sqlite3
# from datetime import datetime
# import plotly.express as px
#
# conn = sqlite3.connect("sheets_data.db")
# df_raw = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', conn)
#
# # Parse dates for filtering and plotting
# df_raw['transaction_date'] = pd.to_datetime(df_raw['transaction_date'])
# # Load precomputed metrics from metrics.json
# with open("metrics.json", "r") as f:
#     metrics = json.load(f)
#
# # Convert to DataFrames
# daily_transactions_df = pd.DataFrame(metrics["daily_transactions"])
# outlet_transactions_df = pd.DataFrame(metrics["outlet_daily_transactions"])
# daily_sales_df = pd.DataFrame(metrics["daily_sales"])
# store_sales_df = pd.DataFrame(metrics["store_sales"])
#
# # Ensure date columns are datetime
# daily_transactions_df["date"] = pd.to_datetime(daily_transactions_df["date"])
# outlet_transactions_df["transaction_date"] = pd.to_datetime(outlet_transactions_df["transaction_date"])
# daily_sales_df["date"] = pd.to_datetime(daily_sales_df["date"])
#
# # Get date range and store list
# min_date = daily_sales_df["date"].min().date()
# max_date = daily_sales_df["date"].max().date()
# store_ids = store_sales_df["store_id"].unique().tolist()
#
# # UI
# st.title("📊 Sales & Transactions Dashboard")
#
# tab1, tab2 = st.tabs(["🧾 Transactions", "💰 Sales"])
#
# # -------------------- TRANSACTIONS TAB --------------------
# with tab1:
#     st.subheader("Transaction Overview")
#
#     # Filters
#     with st.sidebar:
#         st.header("🧮 Transaction Filters")
#         selected_store_txn = st.selectbox("Store ID (Transactions)", options=["All"] + store_ids)
#         selected_txn_range = st.date_input("Transaction Date Range", [min_date, max_date], key="txn")
#
#     # Filter raw data
#     txn_mask = (df_raw['transaction_date'].dt.date >= selected_txn_range[0]) & \
#                (df_raw['transaction_date'].dt.date <= selected_txn_range[1])
#
#     if selected_store_txn != "All":
#         txn_mask &= (df_raw['sales_outlet_id'] == selected_store_txn)
#
#     txn_filtered = df_raw[txn_mask]
#
#     # Total filtered transactions
#     st.metric("Filtered Transactions", txn_filtered.shape[0])
#
#     # Daily transaction trend (filtered)
#     txn_daily = (
#         txn_filtered.groupby(txn_filtered['transaction_date'].dt.date)['transaction_id']
#         .count()
#         .reset_index()
#     )
#     txn_daily.columns = ['date', 'transactions']
#     txn_daily['date'] = pd.to_datetime(txn_daily['date'])
#
#     st.subheader(f"Daily Transaction Trend - Store {selected_store_txn}")
#     st.line_chart(txn_daily.set_index("date")["transactions"])
#
# # -------------------- SALES TAB --------------------
# with tab2:
#     st.subheader("Sales Overview")
#
#     # Filters
#     with st.sidebar:
#         st.header("💡 Sales Filters")
#         selected_store = st.selectbox("Store ID", options=["All"] + store_ids)
#         selected_range = st.date_input("Date Range", [min_date, max_date])
#
#     # Load full transaction data for accurate filtering
#     df_raw = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', sqlite3.connect("sheets_data.db"))
#     df_raw['transaction_date'] = pd.to_datetime(df_raw['transaction_date'])
#     df_raw['sales'] = df_raw['quantity'] * df_raw['unit_price']
#
#     # Apply filters to raw data
#     mask = (df_raw['transaction_date'].dt.date >= selected_range[0]) & \
#            (df_raw['transaction_date'].dt.date <= selected_range[1])
#
#     if selected_store != "All":
#         mask &= (df_raw['sales_outlet_id'] == selected_store)
#
#     filtered = df_raw[mask]
#
#     # Total filtered sales
#     total_filtered_sales = filtered['sales'].sum()
#     st.metric("Filtered Total Sales", f"${total_filtered_sales:,.2f}")
#
#     # Daily sales for filtered data
#     daily_filtered_sales = (
#         filtered.groupby(filtered['transaction_date'].dt.date)['sales']
#         .sum()
#         .reset_index()
#     )
#     daily_filtered_sales.columns = ['date', 'sales']
#     daily_filtered_sales['date'] = pd.to_datetime(daily_filtered_sales['date'])
#
#     st.subheader(f"Daily Sales Trend - store {selected_store}")
#     st.line_chart(daily_filtered_sales.set_index("date")["sales"])
#
#     if selected_store == "All":
#         st.subheader("Store-wise Total Sales")
#         st.bar_chart(store_sales_df.set_index("store_id")["sales"])

#
# import streamlit as st
# import pandas as pd
# import json
# import sqlite3
# from datetime import datetime
# import plotly.express as px
#
# conn = sqlite3.connect("sheets_data.db")
# df_raw = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', conn)
#
# # Parse dates for filtering and plotting
# df_raw['transaction_date'] = pd.to_datetime(df_raw['transaction_date'])
# df_raw['sales'] = df_raw['quantity'] * df_raw['unit_price']
#
# # Load precomputed metrics from metrics.json
# with open("metrics.json", "r") as f:
#     metrics = json.load(f)
#
# # Convert to DataFrames
# daily_transactions_df = pd.DataFrame(metrics["daily_transactions"])
# outlet_transactions_df = pd.DataFrame(metrics["outlet_daily_transactions"])
# daily_sales_df = pd.DataFrame(metrics["daily_sales"])
# store_sales_df = pd.DataFrame(metrics["store_sales"])
#
# # Ensure date columns are datetime
# daily_transactions_df["date"] = pd.to_datetime(daily_transactions_df["date"])
# outlet_transactions_df["transaction_date"] = pd.to_datetime(outlet_transactions_df["transaction_date"])
# daily_sales_df["date"] = pd.to_datetime(daily_sales_df["date"])
#
# # Get date range, store list, and product list
# # Get date range, store list, and product list
# min_date = daily_sales_df["date"].min().date()
# max_date = daily_sales_df["date"].max().date()
# store_ids = sorted(store_sales_df["store_id"].unique().tolist())  # sorted
# product_ids = sorted(df_raw["product_id"].unique().tolist())      # sorted
#
#
# # UI
# st.title("📊 Sales & Transactions Dashboard")
#
# tab1, tab2, tab3 = st.tabs(["🧾 Transactions", "💰 Sales", "📈 Other KPI's"])
#
# # -------------------- TRANSACTIONS TAB --------------------
# with tab1:
#     st.subheader("Transaction Overview")
#     st.metric("Total Transactions", metrics["total_transactions"])
#
#     # Filters
#     with st.sidebar:
#         st.header("🧾 Transaction Filters")
#         selected_store_txn = st.selectbox("Store ID (Transactions)", options=["All"] + store_ids)
#         selected_product_txn = st.selectbox("Product ID (Transactions)", options=["All"] + product_ids)
#         selected_range_txn = st.date_input("Transaction Date Range", [min_date, max_date], key="txn")
#
#     # Apply filters
#     mask_txn = (df_raw['transaction_date'].dt.date >= selected_range_txn[0]) & \
#                (df_raw['transaction_date'].dt.date <= selected_range_txn[1])
#     if selected_store_txn != "All":
#         mask_txn &= df_raw['sales_outlet_id'] == selected_store_txn
#     if selected_product_txn != "All":
#         mask_txn &= df_raw['product_id'] == selected_product_txn
#
#     filtered_txn = df_raw[mask_txn]
#
#     st.metric("Filtered Transactions", len(filtered_txn))
#
#     # Group and prepare transaction trend
#     transactions_by_store = (
#         filtered_txn.groupby(filtered_txn['transaction_date'].dt.date)['transaction_id']
#         .count()
#         .reset_index()
#         .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
#     )
#     transactions_by_store['date'] = pd.to_datetime(transactions_by_store['date'])
#
#     transactions_by_store = transactions_by_store.rename(columns={"transaction_date": "date"})
#
#     st.subheader("Filtered Daily Transaction Trend")
#     st.line_chart(transactions_by_store.set_index("date")["transactions"])
#
# # -------------------- SALES TAB --------------------
# with tab2:
#     st.subheader("Sales Overview")
#
#     # Filters
#     with st.sidebar:
#         st.header("💡 Sales Filters")
#         selected_store = st.selectbox("Store ID (Sales)", options=["All"] + store_ids, key="sales_store")
#         selected_product = st.selectbox("Product ID (Sales)", options=["All"] + product_ids, key="sales_product")
#         selected_range = st.date_input("Sales Date Range", [min_date, max_date], key="sales")
#
#     # Apply filters to raw data
#     mask = (df_raw['transaction_date'].dt.date >= selected_range[0]) & \
#            (df_raw['transaction_date'].dt.date <= selected_range[1])
#
#     if selected_store != "All":
#         mask &= (df_raw['sales_outlet_id'] == selected_store)
#
#     if selected_product != "All":
#         mask &= (df_raw['product_id'] == selected_product)
#
#     filtered = df_raw[mask]
#
#     # Filtered sales total
#     st.metric("Filtered Total Sales", f"${filtered['sales'].sum():,.2f}")
#
#     # Daily sales for filtered data
#     daily_filtered_sales = (
#         filtered.groupby(filtered['transaction_date'].dt.date)['sales']
#         .sum()
#         .reset_index()
#     )
#     daily_filtered_sales.columns = ['date', 'sales']
#     daily_filtered_sales['date'] = pd.to_datetime(daily_filtered_sales['date'])
#
#     st.subheader(f"Filtered Daily Sales Trend - store {selected_store}")
#     st.line_chart(daily_filtered_sales.set_index("date")["sales"])
#
#     if selected_store == "All":
#         st.subheader("Store-wise Total Sales")
#         st.bar_chart(store_sales_df.set_index("store_id")["sales"])




# import streamlit as st
# import pandas as pd
# import json
# import sqlite3
# from datetime import datetime
# import plotly.express as px
#
# conn = sqlite3.connect("sheets_data.db")
# df_raw = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', conn)
#
# # Parse dates for filtering and plotting
# df_raw['transaction_date'] = pd.to_datetime(df_raw['transaction_date'])
# df_raw['sales'] = df_raw['quantity'] * df_raw['unit_price']
#
# # Load precomputed metrics from metrics.json
# with open("metrics.json", "r") as f:
#     metrics = json.load(f)
#
# # Convert to DataFrames
# daily_transactions_df = pd.DataFrame(metrics["daily_transactions"])
# outlet_transactions_df = pd.DataFrame(metrics["outlet_daily_transactions"])
# daily_sales_df = pd.DataFrame(metrics["daily_sales"])
# store_sales_df = pd.DataFrame(metrics["store_sales"])
#
# # Ensure date columns are datetime
# daily_transactions_df["date"] = pd.to_datetime(daily_transactions_df["date"])
# outlet_transactions_df["transaction_date"] = pd.to_datetime(outlet_transactions_df["transaction_date"])
# daily_sales_df["date"] = pd.to_datetime(daily_sales_df["date"])
#
# # Get date range, store list, and product list
# min_date = daily_sales_df["date"].min().date()
# max_date = daily_sales_df["date"].max().date()
# store_ids = sorted(store_sales_df["store_id"].unique().tolist())
# product_ids = sorted(df_raw["product_id"].unique().tolist())
#
# # UI
# st.title("📊 Sales & Transactions Dashboard")
#
# tab1, tab2, tab3 = st.tabs(["🧾 Transactions", "💰 Sales", "📈 Other KPI's"])
#
# # -------------------- TRANSACTIONS TAB --------------------
# with tab1:
#     st.subheader("Transaction Overview")
#     st.metric("Total Transactions", metrics["total_transactions"])
#
#     # Filters
#     with st.sidebar:
#         st.header("🧾 Transaction Filters")
#         selected_store_txn = st.multiselect("Store ID (Transactions)", options=["All"] + store_ids, default="All")
#         selected_product_txn = st.multiselect("Product ID (Transactions)", options=["All"] + product_ids, default="All")
#         selected_range_txn = st.date_input("Transaction Date Range", [min_date, max_date], key="txn")
#
#     # Apply filters
#     mask_txn = (df_raw['transaction_date'].dt.date >= selected_range_txn[0]) & \
#                (df_raw['transaction_date'].dt.date <= selected_range_txn[1])
#
#     if "All" not in selected_store_txn:
#         mask_txn &= df_raw['sales_outlet_id'].isin(selected_store_txn)
#
#     if "All" not in selected_product_txn:
#         mask_txn &= df_raw['product_id'].isin(selected_product_txn)
#
#     filtered_txn = df_raw[mask_txn]
#
#     st.metric("Filtered Transactions", len(filtered_txn))
#
#     # Group and prepare transaction trend
#     transactions_by_store = (
#         filtered_txn.groupby(filtered_txn['transaction_date'].dt.date)['transaction_id']
#         .count()
#         .reset_index()
#         .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
#     )
#     transactions_by_store['date'] = pd.to_datetime(transactions_by_store['date'])
#
#     st.subheader("Filtered Daily Transaction Trend")
#     st.line_chart(transactions_by_store.set_index("date")["transactions"])
#
# # -------------------- SALES TAB --------------------
# with tab2:
#     st.subheader("Sales Overview")
#
#     # Filters
#     with st.sidebar:
#         st.header("💡 Sales Filters")
#         selected_store = st.multiselect("Store ID (Sales)", options=["All"] + store_ids, default="All", key="sales_store")
#         selected_product = st.multiselect("Product ID (Sales)", options=["All"] + product_ids, default="All", key="sales_product")
#         selected_range = st.date_input("Sales Date Range", [min_date, max_date], key="sales")
#
#     # Apply filters to raw data
#     mask = (df_raw['transaction_date'].dt.date >= selected_range[0]) & \
#            (df_raw['transaction_date'].dt.date <= selected_range[1])
#
#     if "All" not in selected_store:
#         mask &= df_raw['sales_outlet_id'].isin(selected_store)
#
#     if "All" not in selected_product:
#         mask &= df_raw['product_id'].isin(selected_product)
#
#     filtered = df_raw[mask]
#
#     # Filtered sales total
#     st.metric("Filtered Total Sales", f"${filtered['sales'].sum():,.2f}")
#
#     # Daily sales for filtered data
#     daily_filtered_sales = (
#         filtered.groupby(filtered['transaction_date'].dt.date)['sales']
#         .sum()
#         .reset_index()
#     )
#     daily_filtered_sales.columns = ['date', 'sales']
#     daily_filtered_sales['date'] = pd.to_datetime(daily_filtered_sales['date'])
#
#     st.subheader("Filtered Daily Sales Trend")
#     st.line_chart(daily_filtered_sales.set_index("date")["sales"])
#
#     if selected_store == ["All"]:
#         st.subheader("Store-wise Total Sales")
#         st.bar_chart(store_sales_df.set_index("store_id")["sales"])


import streamlit as st
import pandas as pd
import json
import sqlite3
from datetime import datetime
import plotly.express as px

conn = sqlite3.connect("sheets_data.db")
df_raw = pd.read_sql_query('SELECT * FROM "201904_sales_reciepts"', conn)

# Parse dates for filtering and plotting
df_raw['transaction_date'] = pd.to_datetime(df_raw['transaction_date'])
df_raw['sales'] = df_raw['quantity'] * df_raw['unit_price']

# Load precomputed metrics from metrics.json
with open("metrics.json", "r") as f:
    metrics = json.load(f)

# Convert to DataFrames
daily_transactions_df = pd.DataFrame(metrics["daily_transactions"])
outlet_transactions_df = pd.DataFrame(metrics["outlet_daily_transactions"])
daily_sales_df = pd.DataFrame(metrics["daily_sales"])
store_sales_df = pd.DataFrame(metrics["store_sales"])

# Ensure date columns are datetime
daily_transactions_df["date"] = pd.to_datetime(daily_transactions_df["date"])
outlet_transactions_df["transaction_date"] = pd.to_datetime(outlet_transactions_df["transaction_date"])
daily_sales_df["date"] = pd.to_datetime(daily_sales_df["date"])

# Get date range, store list, and product list
min_date = daily_sales_df["date"].min().date()
max_date = daily_sales_df["date"].max().date()
store_ids = sorted(store_sales_df["store_id"].unique().tolist())
product_ids = sorted(df_raw["product_id"].unique().tolist())

# UI
st.title("📊 Sales & Transactions Dashboard")

tab1, tab2, tab3 = st.tabs(["🧾 Transactions", "💰 Sales", "🍵 Products"])

# -------------------- TRANSACTIONS TAB --------------------
with tab1:
    st.subheader("Transaction Overview")
    st.metric("Total Transactions", metrics["total_transactions"])

    # Filters
    with st.sidebar:
        st.header("🧾 Transaction Filters")
        selected_store_txn = st.selectbox(
            "Store ID (Transactions)",
            options=["All"] + store_ids,
            index=None,
            placeholder="Select or type Store ID"
        )
        selected_product_txn = st.selectbox(
            "Product ID (Transactions)",
            options=["All"] + product_ids,
            index=None,
            placeholder="Select or type Product ID"
        )
        selected_range_txn = st.date_input("Transaction Date Range", [min_date, max_date], key="txn")

    # Apply filters
    mask_txn = (df_raw['transaction_date'].dt.date >= selected_range_txn[0]) & \
               (df_raw['transaction_date'].dt.date <= selected_range_txn[1])

    if selected_store_txn and selected_store_txn != "All":
        mask_txn &= df_raw['sales_outlet_id'] == selected_store_txn

    if selected_product_txn and selected_product_txn != "All":
        mask_txn &= df_raw['product_id'] == selected_product_txn

    filtered_txn = df_raw[mask_txn]
    st.metric("Filtered Transactions", len(filtered_txn))

    # Group and prepare transaction trend
    transactions_by_store = (
        filtered_txn.groupby(filtered_txn['transaction_date'].dt.date)['transaction_id']
        .count()
        .reset_index()
        .rename(columns={'transaction_id': 'transactions', 'transaction_date': 'date'})
    )
    transactions_by_store['date'] = pd.to_datetime(transactions_by_store['date'])

    st.subheader("Filtered Daily Transaction Trend")
    st.line_chart(transactions_by_store.set_index("date")["transactions"])

# -------------------- SALES TAB --------------------
with tab2:
    st.subheader("Sales Overview")

    # Filters
    with st.sidebar:
        st.header("💡 Sales Filters")
        selected_store = st.selectbox(
            "Store ID (Sales)",
            options=["All"] + store_ids,
            index=None,
            placeholder="Select or type Store ID",
            key="sales_store"
        )
        selected_product = st.selectbox(
            "Product ID (Sales)",
            options=["All"] + product_ids,
            index=None,
            placeholder="Select or type Product ID",
            key="sales_product"
        )
        selected_range = st.date_input("Sales Date Range", [min_date, max_date], key="sales")

    # Apply filters to raw data
    mask = (df_raw['transaction_date'].dt.date >= selected_range[0]) & \
           (df_raw['transaction_date'].dt.date <= selected_range[1])

    if selected_store and selected_store != "All":
        mask &= (df_raw['sales_outlet_id'] == selected_store)

    if selected_product and selected_product != "All":
        mask &= (df_raw['product_id'] == selected_product)

    filtered = df_raw[mask]

    # Filtered sales total
    st.metric("Filtered Total Sales", f"${filtered['sales'].sum():,.2f}")

    # Daily sales for filtered data
    daily_filtered_sales = (
        filtered.groupby(filtered['transaction_date'].dt.date)['sales']
        .sum()
        .reset_index()
    )
    daily_filtered_sales.columns = ['date', 'sales']
    daily_filtered_sales['date'] = pd.to_datetime(daily_filtered_sales['date'])

    st.subheader(f"Filtered Daily Sales Trend - store {selected_store}")
    st.line_chart(daily_filtered_sales.set_index("date")["sales"])

    if selected_store == "All" or selected_store is None:
        st.subheader("Store-wise Total Sales")
        st.bar_chart(store_sales_df.set_index("store_id")["sales"])
