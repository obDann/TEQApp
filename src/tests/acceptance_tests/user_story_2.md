# User story 2
The user story that is going to be covered is the following:  
**As a volunteer for agency XYZ, Sam Spongy, I want to be able to upload any of the 8 different types of iCare excel files so that the agency that I represent can contribute to the CCS program.**


This user story is about the feature to upload an excel file which follows one of the eight iCare templates in order to upload their own agency's data. This user story has been completed and to test out the feature as a user, follow the steps below:

### Creating an agency account and logging in
  1. Run the line `python3 main.py` in commandline while in the directory `/src/main`.
  2. Click the button labeled `Create a New Account`.
  3. Fill in all the fields as required and select the account type labeled `Agency`, then click `Submit`.
  4. Click the `Login` button and log into your account with the credentials used to create the account.
  5. Click the `Login` button again and you will be logged into your account.

### Uploading files
  6. Click the `Submit iCare File` button and you will be prompted with 8 different types of files to upload.
  7. Select any of the buttons (except than `Back`) and a file traverser window will open up.
  8. Select a file which complies with the respective template format, then a window may pop up asking what sheet you would like to upload if there are multiple sheets.
  9. When the sheet is selected, the program will give you an option to select a date.
  10. After selecting the date for uploading, it will take you to a table viewer page within the GUI where you can generate a table. Click `Generate Table`.
  11. After generating the table, you will finally be able to upload your file by clicking `Upload` assuming there are no errors within the file uploaded.

After performing the 11 steps above, you will have successfully uploaded your file into the database.
