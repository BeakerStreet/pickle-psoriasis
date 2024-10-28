import gspread
from google.oauth2.service_account import Credentials

def save_job_posting_url_to_gsheet(url, spreadsheet_id, sheet_name):
    # Define the scope
    scope = ["https://www.googleapis.com/auth/spreadsheets"]

    # Add your service account file path
    creds = Credentials.from_service_account_file('path/to/your/service_account.json', scopes=scope)

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
