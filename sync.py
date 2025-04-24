# import gspread
# from google.oauth2.service_account import Credentials
#
# scopes =[
#     "https://www.googleapis.com/auth/spreadsheets"
#
# ]
# creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
#
# client = gspread.authorize(creds)
#
# sheet_id = "1jUg3Rh0Dh2jJHKt3JcBMrdBkJi3SfvjUayJmucEZ0AQ"
#
# sheet = client.open_by_key(sheet_id)
#
# values_list = sheet.sheet1.row_values(1)
# print(values_list)
# import gspread
# from google.oauth2.service_account import Credentials
#
# # Define scopes
# scopes = ["https://www.googleapis.com/auth/spreadsheets"]
# creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
#
# # Authorize the client
# client = gspread.authorize(creds)
#
# # Your Google Sheet ID (not the name, but the long string from the URL)
# sheet_id = "1jUg3Rh0Dh2jJHKt3JcBMrdBkJi3SfvjUayJmucEZ0AQ"
# spreadsheet = client.open_by_key(sheet_id)
#
# # Loop through all 9 sheets
# for worksheet in spreadsheet.worksheets():
#     print(f"Sheet Title: {worksheet.title}")
#     row_values = worksheet.row_values(1)
#     print(f"First row: {row_values}")
#     print("-" * 40)
# import gspread
# import sqlite3
# import pandas as pd
# from google.oauth2.service_account import Credentials
#
# # Define scopes
# scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
# creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
#
# # Authorize the client
# client = gspread.authorize(creds)
#
# # Connect to SQLite database (or create it)
# conn = sqlite3.connect("sheets_data.db")
#
#
# # Your Google Sheet ID (from the URL)
# sheet_id = "1jUg3Rh0Dh2jJHKt3JcBMrdBkJi3SfvjUayJmucEZ0AQ"
# spreadsheet = client.open_by_key(sheet_id)
#
# # Loop through all 9 sheets
# for worksheet in spreadsheet.worksheets():
#     print(f"Importing sheet: {worksheet.title}")
#
#     # Convert the sheet to a DataFrame
#     data = worksheet.get_all_records()
#     df = pd.DataFrame(data)
#
#     # Save to SQLite, using the sheet title as the table name
#     table_name = worksheet.title.replace(" ", "_")  # Table names can't have spaces
#     df.to_sql(table_name, conn, if_exists="replace", index=False)
#
#     print(f"Saved to table: {table_name}")
#     print("-" * 40)
#
# conn.close()
# print("All sheets imported and saved to database.")
#
import gspread
import pandas as pd
import sqlite3
from google.oauth2.service_account import Credentials

# Define Google Sheets API scopes
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)

# Authorize the client
client = gspread.authorize(creds)

# Your Google Sheet ID (from the URL)
sheet_id = "1jUg3Rh0Dh2jJHKt3JcBMrdBkJi3SfvjUayJmucEZ0AQ"
spreadsheet = client.open_by_key(sheet_id)

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("sheets_data.db")

# Loop through all worksheets and save to DB
for worksheet in spreadsheet.worksheets():
    print(f"\n⏳ Syncing sheet: {worksheet.title}")
    data = worksheet.get_all_records()
    if data:
        df = pd.DataFrame(data)
        print(f"✅ Loaded {len(df)} rows from '{worksheet.title}'")
        table_name = worksheet.title.replace(" ", "_").lower()
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"📥 Stored as table: {table_name}")
    else:
        print(f"⚠️ No data found in '{worksheet.title}'")

# List all tables in the database
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("\n📄 Tables in database:")
for t in tables:
    print(" -", t[0])

# Close DB connection
conn.close()
