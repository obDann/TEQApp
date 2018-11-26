# User story 6
The user story that is going to be covered is the following:  
**As a long-term TEQ employee, Louis Chan, I want to be able to create custom queries by selecting from a list of variables from a drop down bar so that I can customize the data I want to see.**


This user story is about the feature to select custom queries according to the data and generating a custom graph based on the selected attributes. This user story has been completed and to test out the feature as a user, follow the steps below:

### Creating an agency account
  1. Run the line `python3 main.py` in commandline while in the directory `/src/main`.
  2. Click the button labeled `Create a New Account`.
  3. Fill in all the fields as required and select the account type labeled `Agency`, then click `Submit`.

### Creating a TEQ account
  4. Click the button labeled `Create a New Account`.
  5. Fill in all the fields as required (different from the account created previously) and select the account type labeled `TEQ`, then click `Submit`.

### Log into the agency account and upload files
  6. Click the `Login` button and log into the agency account you created and click `Login` again.
  7. Next, select `Submit iCare File` and select `Client Profile`.
  8. Upload the correct file for client profile, and then a window may pop up asking what sheet you would like to upload if there are multiple sheets.
  9. When the sheet is selected, the program will give you an option to select a date.
  10. After selecting the date for uploading, it will take you to a table viewer page within the GUI where you can generate a table. Click `Generate Table`.
  11. After generating the table, you will finally be able to upload your file by clicking `Upload` assuming there are no errors within the file uploaded.
  12. Repeat steps 7-11 for multiple other data files and be sure to upload the correct file for that respective type.

### Log into the TEQ account and generate custom query
  13. Click `Back` to log out of the agency account.
  14. Click the `Login` button and log into the TEQ account you created and click `Login` again.
  15. Select `Generate Reports` and then select `Answer Research Questions`.
  16. Click `Service Reports` and you will be able to select multiple values from dropdown bars to generate reports.
  17. After you confirm which reports and services you would like to view, click `Generate Report` and a graph will pop up based on the fields you selected.

After performing the 17 steps above, there should be a generated graph that pops up which shows trends in the data sets selected.
