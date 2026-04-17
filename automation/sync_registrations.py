"""
Swops Registration Sync
Pulls new Netlify form submissions and adds them to Google Sheets.
Runs on a schedule - no manual intervention needed.
"""
import warnings
warnings.filterwarnings('ignore')

import os, json, datetime
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import urllib.request

BASE        = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE  = os.path.join(BASE, 'credentials/token.json')
CONFIG_FILE = os.path.join(BASE, 'config.json')

with open(CONFIG_FILE) as f:
    config = json.load(f)

SHEET_ID        = config['registration_sheet_id']
NETLIFY_TOKEN   = config.get('netlify_token', '')
NETLIFY_FORM_ID = config.get('netlify_form_id', '')

creds = Credentials.from_authorized_user_file(TOKEN_FILE)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())
    with open(TOKEN_FILE, 'w') as f:
        f.write(creds.to_json())

sheets = build('sheets', 'v4', credentials=creds)

def get_existing_emails():
    result = sheets.spreadsheets().values().get(
        spreadsheetId=SHEET_ID, range='Registrations!C2:C'
    ).execute()
    return set(r[0].lower() for r in result.get('values', []) if r)

NEW_HEADERS = ['Phone', 'Address', 'Best Thing', 'Pets', 'Parking', 'Want', 'Place Type', 'Questions']

def ensure_headers():
    """Make sure columns O-V have headers for the newer form fields."""
    result = sheets.spreadsheets().values().get(
        spreadsheetId=SHEET_ID, range='Registrations!O1:V1'
    ).execute()
    existing = result.get('values', [[]])[0]
    if existing != NEW_HEADERS:
        sheets.spreadsheets().values().update(
            spreadsheetId=SHEET_ID,
            range='Registrations!O1:V1',
            valueInputOption='RAW',
            body={'values': [NEW_HEADERS]}
        ).execute()
        print('Added new column headers O-V.')

def append_row(row):
    sheets.spreadsheets().values().append(
        spreadsheetId=SHEET_ID,
        range='Registrations!A:V',
        valueInputOption='USER_ENTERED',
        insertDataOption='INSERT_ROWS',
        body={'values': [row]}
    ).execute()

def fetch_submissions():
    url = f'https://api.netlify.com/api/v1/forms/{NETLIFY_FORM_ID}/submissions?access_token={NETLIFY_TOKEN}'
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read())

def run():
    ensure_headers()
    existing = get_existing_emails()
    submissions = fetch_submissions()
    new_count = 0

    for sub in submissions:
        data  = sub.get('data', {})
        email = (data.get('email') or '').strip().lower()
        if not email or email in existing:
            continue

        ts = datetime.datetime.fromisoformat(
            sub.get('created_at', '').replace('Z', '+00:00')
        ).strftime('%d %b %Y %H:%M') if sub.get('created_at') else datetime.datetime.now().strftime('%d %b %Y %H:%M')

        row = [
            ts,                                    # A: Timestamp
            data.get('name', '').strip(),           # B: Name
            email,                                  # C: Email
            data.get('suburb', '').strip(),          # D: Suburb
            data.get('house-type', '').strip(),      # E: House Type
            data.get('bedrooms', '').strip(),        # F: Bedrooms
            '',                                     # G: People (legacy, kept for alignment)
            data.get('rating', '').strip(),          # H: Rating
            data.get('song', '').strip(),            # I: Song
            data.get('walk-to', '').strip(),         # J: Walk To
            'New', '', '',                           # K: Status, L: Matched With, M: Notes
            '',                                     # N: Listing URL (filled by create_listing.py)
            data.get('phone', '').strip(),           # O: Phone
            data.get('address', '').strip(),         # P: Address
            data.get('best-thing', '').strip(),      # Q: Best Thing
            data.get('pets', '').strip(),            # R: Pets
            data.get('parking', '').strip(),         # S: Parking
            data.get('want', '').strip(),            # T: Want
            data.get('place-type', '').strip(),      # U: Place Type
            data.get('questions', '').strip(),       # V: Questions
        ]
        append_row(row)
        existing.add(email)
        new_count += 1
        print(f'Added: {data.get("name","?")} <{email}>')

    print(f'{new_count} new registration(s) added.')

if __name__ == '__main__':
    run()
