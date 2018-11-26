# User story 2
The user story that is going to be covered is the following:  
**As a volunteer for agency XYZ, Sam Spongy, I expect that when I upload my data, all entries are automatically formatted to comply with the system’s format so that I do not have to manually change any entries.**


This user story is about the feature where, when uploading a file, the program will upload the data no matter how different the file is formatted to the recommended one (i.e., a value within postal code wont necessarily be within the X1X1X1 format, but it will be properly uploaded). This user story has been completed and to test out the feature as a user, follow the steps below:

### Creating an agency account and logging in
  1. Run the line `python3 main.py` in commandline while in the directory `/src/main`.
  2. Click the button labeled `Create a New Account`.
  3. Fill in all the fields as required and select the account type labeled `Agency`, then click `Submit`.
  4. Click the `Login` button and log into your account with the credentials used to create the account.
  5. Click the `Login` button again and you will be logged into your account.

### Uploading files
  6. Click the `Submit iCare File` button and you will be prompted with 8 different types of files to upload.
  7. Select any of the buttons (except than `Back`) and a file traverser window will open up.
  8. Select a file which does not fully comply by the respective template format, and then a window may pop up asking what sheet you would like to upload if there are multiple sheets.
  9. When the sheet is selected, the program will give you an option to select a date.
  10. After selecting the date for uploading, it will take you to a table viewer page within the GUI where you can generate a table. Click `Generate Table`.
  11. After generating the table, you will finally be able to upload your file by clicking `Upload` assuming there are no errors within the file uploaded.

After performing the steps above, the user's data will be uploaded properly despite having a differing format than the recommended one.
