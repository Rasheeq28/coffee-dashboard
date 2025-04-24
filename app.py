import streamlit as st
from sync import sheets_data

st.title("📊 Google Sheets Live Dashboard")

# Example: show one sheet
selected_sheet = st.selectbox("Choose a Sheet", list(sheets_data.keys()))
st.dataframe(sheets_data[selected_sheet])
