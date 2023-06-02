# gdrive-upload
Google Drive Upload a File

## Download Packages
```sh
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Create your Account Service Key File
You can obtain a service account key file by following these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

2. If you haven't already, sign in with your Google account and create a new project or select an existing one.

3. In the left sidebar menu, click on "IAM & Admin" and then "Service accounts."

4. Click "Create Service Account" at the top of the page.

5. Fill in the required information for the new service account (e.g., name, description), and click "Create."

6. In the "Select a role" dropdown, search for "Drive" and choose a suitable role, such as "Drive File Stream." Note that this role may be overly permissive, so you might want to create a custom role with more limited permissions depending on your needs. Click "Continue."

7. On the "Grant users access to this service account" page, you can add members and define roles for them if needed. Click "Done."

8. Now you should see the created service account in the list. Click on the pencil/edit icon to view and manage the service account details.

9. In the "Keys" tab, click "Add Key" and choose "JSON."

10. A JSON key file will be generated and downloaded automatically. This is the service account key file that you can use in the script provided earlier.

Make sure to keep the downloaded key file secure, as it contains sensitive information that can be used to access your Google Cloud resources. Do not share it publicly or include it in version control systems like Git.

## Use The Program
After downloading service account key json as service-account-key.json or changing name in the code as you wish. run this commands:
```sh
root@server:~# python3 uploader.py file.zip 
Uploading file: file.zip
File ID: a-google-drive-file-id
```
