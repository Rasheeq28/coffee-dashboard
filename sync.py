import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe



# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open your Google Sheet
spreadsheet = client.open("Project 01")

# Fetch all 9 sheets
sheet_titles = [ws.title for ws in spreadsheet.worksheets()]
sheets_data = {}

for title in sheet_titles:
    worksheet = spreadsheet.worksheet(title)
    df = get_as_dataframe(worksheet, evaluate_formulas=True, dtype=str)
    df.dropna(how="all", inplace=True)  # Clean empty rows
    sheets_data[title] = df

# Optional: print to verify
for name, df in sheets_data.items():
    print(f"\nSheet: {name}\n", df.head())
