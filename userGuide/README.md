# User Manual
1. After finishing setting up, you are ready to run this application. Within the [src/main](../src/main) folder, run `python3 main.py` in your terminal or on your favorite IDE. The main page of the application will pop up: 
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/0.png)
If this is your first time using this application, create a new account by clicking "Create a New Account". It will take you to this:
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/1.png)
After you finish filling this form in, click "Submit" and it will take you back to the main page if your account was successfully created.
2. In the main page, Click "Login" and enter your username and password:
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/3.png)
If you forgot your password, click "Forgot Password?" and enter your email. A temporary password will be sent to your email and you can use that temporary password to login and to reset your password.
3. After successfully logging in, if your account is an "agency" account, this page will show up:
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/4.png)
An agency account can submit iCare templates into the system to be used for reports. To submit a template, click "Submit iCare File" and it will bring you to this:
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/5.png)
Select the template you want to submit and a window will pop up where you can select the file in your computer to submit. After selecting the right file, enter the month and year this templates data corresponds to:
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/6.png)
After selecting the month and year and pressing "Select", this page will show up:
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/7.png)
Clicking "Generate Table" will allow you to view the data you have and you can make any changes before you submit.
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/9.png)
If you are satisfied with your file, press "Upload" to submit the file.
4. For a "TEQ" account, after logging in it will bring you to this page:
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/11.png)
A TEQ account can generate reports with the data that Agency accounts submitted, or they can remove any agency accounts if an agency has closed down. To remove an agency account, click "Delete Account" and type the username of the agency you want to remove. To generate reports click "Generate Reports" and it will bring you to this page:
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/12.png)

In "Answer Research Questions", you can view and download some reports that correspond to the current topics in demand. Here are some examples:
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/hist.png)
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/pie.png)

If you want to generate your own reports, click "Generate Custom Queries" and it will take you to this page:
![alt text](https://github.com/CSCC01/Team10/blob/master/userGuide/pics/13.png)
An ER Diagram has been provided in [this](./) directory called "diagram.pdf". It shows the tables in the database and the relations between each entity. Using this diagram, you can create your own SQL query and enter it into the text box, then choose a name for the file. Press "Save" to generate the query. If the query was successful, you should be able to see a .csv file in the main directory which contains the output of your query.

In "Predictive Analysis",
