from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow, Flow
from google.auth.transport.requests import Request
import os
import pickle

RANGE = 'A1:AA20000'
SPREADSHEET_ID = ''

def Create_Service(client_secret_file, api_service_name, api_version, *scopes):
    global service
    SCOPES = ''
    cred = None

    if (os.path.exists('token_write.pickle')):
        with open('token_write.pickle', 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())

        else:
            flow = InstalledAppFlow.from_clients_secrets_file(client_secret_file, SCOPES)
            cred = flow.run_local_server()

        with open('token_write.pickle', 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(api_service_name, api_version, credentials=cred)
        print(api_service_name, 'service created successfully')

    except Exception as e:
        print(e)

# Exports data to google sheets
def Export_Data(gsheetId, df):
    response = service.spreadsheets().values().update(
        spreadsheetId = gsheetId,
        valueInputOptions = 'RAW'
        range = RANGE,
        body = dict(
            majorDimension = 'ROWS',
            values = df.T.reset_index().T.values.tolist())
        ).execute()
    print('Sheet successfully updated')
        
