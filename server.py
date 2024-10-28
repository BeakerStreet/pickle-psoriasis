import gspread
from google.oauth2.service_account import Credentialss
import os
from pathlib import Path

def save_job_posting_url_to_gsheet(url, spreadsheet_id, sheet_name):
    # Define the scope
    scope = ["https://www.googleapis.com/auth/spreadsheets"]

    # Look for credentials file in a more reliable way
    creds_path = Path(__file__).parent / 'credentials' / 'service_account.json'
    
    if not creds_path.exists():
        raise FileNotFoundError(f"Please place your Google service account credentials at: {creds_path}")

    # Authorize using the credentials file
    creds = Credentials.from_service_account_file(str(creds_path), scopes=scope)

    # Authorize the client
    client = gspread.authorize(creds)

    # Open the Google Sheet
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)

    # Append the URL to the sheet
    sheet.append_row([url])

# Example usage
job_posting_url = input("Enter the job posting URL: ")
spreadsheet_id = 'your_spreadsheet_id'  # Replace with your Google Sheet ID
sheet_name = 'Sheet1'  # Replace with your sheet name
save_job_posting_url_to_gsheet(job_posting_url, spreadsheet_id, sheet_name)
