from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account
import os
# i'm fine with it only running for 1 sheet this won't get used a lot anyways


def google_sheets_api_call(service_acount_param, spreadsheet_id, scopes_list:list, format:str, sheet_id:str):
    '''calls the google sheets api to retrive workout data. Takes a service_account_filename, spreadsheet_id and sheet_id, file format and list of scopes
        returns the contense of the api call
    '''
    service_account_file = service_acount_param
    credientials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes_list)
    session = AuthorizedSession(credientials)
    url = (
        f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export"
        )

    params = {
        "format": format,
        "gid" : sheet_id
        }

    response = session.get(url, params=params)
    response.raise_for_status()
    return response.content


    
        
if __name__ == "__main__":
    
    service_account_file = os.environ["SERVICE_ACCOUNT_FILE"]
    spreadsheet_id = os.environ["SPREADSHEET_ID"]
    sheet_id = os.environ["HOME_WORKOUT"]
    
    response_content = google_sheets_api_call(service_account_file, spreadsheet_id, ["https://www.googleapis.com/auth/drive"],"xlsx", sheet_id)
    
    
    with open(f"./api_output/{sheet_id}.xlsx", "wb") as f:
            f.write(response_content)
