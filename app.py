import streamlit as st
import pandas as pd
import sqlite3

# Connect to the SQLite database
def load_table(table_name):
    conn = sqlite3.connect("sheets_data.db")
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

# Get table names from the database
def get_table_names():
    conn = sqlite3.connect("sheets_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tables

st.set_page_config(page_title="Google Sheets Dashboard", layout="wide")
st.title("📊 Google Sheets Dashboard")

# Sidebar for table selection
st.sidebar.header("Select a Table")
tables = get_table_names()
selected_table = st.sidebar.selectbox("Choose a table to view", tables)

# Display data from selected table
if selected_table:
    df = load_table(selected_table)
    st.subheader(f"Table: {selected_table}")
    st.dataframe(df)

    # Basic summary stats
    with st.expander("🔍 Summary Statistics"):
        st.write(df.describe(include='all'))

    # Optional charting if numeric columns exist
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_cols:
        st.sidebar.subheader("Chart Options")
        chart_col = st.sidebar.selectbox("Choose a column to chart", numeric_cols)
        st.line_chart(df[chart_col])
