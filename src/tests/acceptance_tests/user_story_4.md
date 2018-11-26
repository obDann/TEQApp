# User story 4
The user story that is going to be covered is the following:  
**As a volunteer for agency XYZ, Sam Spongy, I want to be able to view any data conflicts (i.e. due to duplicate fields like Child 1, Child 2, etc.) or missing data when uploading, so that I can ensure that the data I uploaded is accurate.**


This user story is about the feature where, when uploading a file, the user will be able to check whether the fields fit within the desired format, i.e. checks whether there are duplicates or missing required values, and fix them within the program. This user story has been completed and to test out the feature as a user, follow the steps below:

### Creating an agency account and logging in
  1. Run the line `python3 main.py` in commandline while in the directory `/src/main`.
  2. Click the button labeled `Create a New Account`.
  3. Fill in all the fields as required and select the account type labeled `Agency`, then click `Submit`.
  4. Click the `Login` button and log into your account with the credentials used to create the account.
  5. Click the `Login` button again and you will be logged into your account.

### Uploading files
  6. Click the `Submit iCare File` button and you will be prompted with 8 different types of files to upload.
  7. Select any of the buttons (except than `Back`) and a file traverser window will open up.
  8. Select a file which does not fully comply by the respective template which was selected, and then a window may pop up asking what sheet you would like to upload if there are multiple sheets.
  9. When the sheet is selected, the program will give you an option to select a date.
  10. After selecting the date for uploading, it will take you to a table viewer page within the GUI where you can generate a table. Click `Generate Table`.
  11. When the table is generated, you will be able to see which columns have missing values. You can select that column and fix any missing values manually. After these changes, click `Save`, and then you may safely upload.

After performing the steps above, users will be able to submit their file after fixing up the data.
