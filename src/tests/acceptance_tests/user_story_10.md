# User story 10
The user story that is going to be covered is the following:  
**As a TEQ employee, Mike James, I want to be able to remove agencies in the event that they close down so we don’t have any irrelevant data.**


This user story is about the feature where a TEQ user can delete any agency account so that they are unable to upload any further data. This user story has been completed and to test out the feature as a user, follow the steps below:

### Creating an agency account
  1. Run the line `python3 main.py` in commandline while in the directory `/src/main`.
  2. Click the button labeled `Create a New Account`.
  3. Fill in all the fields as required and select the account type labeled `Agency`, then click `Submit`.

### Creating a TEQ account
  4. Click the button labeled `Create a New Account`.
  5. Fill in all the fields as required (different from the account created previously) and select the account type labeled `TEQ`, then click `Submit`.

### Logging into the TEQ account and deleting the agency account
  6. Click the `Login` button and log into your account with the credentials used to create the TEQ account.
  7. Click the `Login` button again and you will be logged into your account.
  8. Click `Delete Account` and fill in the username of the agency account you created earlier.
  9. Finally, click `Delete` and the account will be successfully deleted.

After performing the 9 steps above, a prompt will appear notifying the user that the agency account was successfully deleted. A new account may be created with the same username/email of the account that was just deleted.
