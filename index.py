from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
import sys

def main():
    # Replace 'your-service-account-key.json' with the path to your Service Account key file
    credentials = service_account.Credentials.from_service_account_file('your-service-account-key.json')

    # Scopes are defined based on API documentation
    scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/drive.file'])

    # Initialize the Drive API client
    service = build('drive', 'v3', credentials=scoped_credentials)

    # Use the provided file path in the command line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("Please provide a file path in the command line argument.")
        return

    # Upload the file
    try:
        print("Uploading file: %s" % file_path)
        file_metadata = {'name': 'yourfilename.zip'}
        media = MediaFileUpload(file_path, resumable=True)

        # Perform the request to create a file and upload its contents
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        print("File ID: %s" % file.get('id'))
    except HttpError as error:
        print(f"An error occurred: {error}")
        return

if __name__ == '__main__':
    main()
