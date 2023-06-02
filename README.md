# gdrive-upload

Upload a file to Google Drive using Python and the Google Drive API.

## Installation

Install the required packages using pip:

```sh
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Obtain Service Account Key File

Follow these steps to create a service account key file:

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).

2. Sign in with your Google account and create a new project or select an existing one.

3. In the left sidebar menu, click on "IAM & Admin" and then "Service accounts."

4. Click on "Create Service Account" at the top of the page.

5. Fill in the required information for the new service account (e.g., name, description), and click "Create."

6. In the "Select a role" dropdown, search for "Drive" and choose a suitable role, such as "Drive File Stream." Note that this role may be overly permissive, so you might want to create a custom role with more limited permissions depending on your needs. Click "Continue."

7. On the "Grant users access to this service account" page, add members and define roles if needed. Click "Done."

8. You should now see the created service account in the list. Click the pencil/edit icon to view and manage the service account details.

9. In the "Keys" tab, click "Add Key" and choose "JSON."

10. A JSON key file will be generated and downloaded automatically. This is the service account key file that you can use in the provided script.

**Remember to keep the downloaded key file secure, as it contains sensitive information that can be used to access your Google Cloud resources. Do not share it publicly or include it in version control systems like Git.**

## Usage

After downloading the service account key JSON file and naming it `service-account-key.json` (or updating the name in the script as necessary), run the following command:

```sh
python3 uploader.py file.zip 
```

Output example:
```
Uploading file: file.zip
File ID: a-google-drive-file-id
```
