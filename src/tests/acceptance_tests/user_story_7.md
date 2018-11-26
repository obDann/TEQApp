# User story 7
The user story that is going to be covered is the following:  
**As a long-term TEQ employee, Louis Chan, I want to be able to see any predictive models that are appropriate for a specific subject**

This user story is about the feature to run predicitive models based off of the data in the database. This user story has been completed and to test out the feature as a user, follow the steps below:

### Starting with some data
  0. If there is already data in your database, ignore step 1.
  1. Before getting started, sample data is provided in this directory. Copy and paste the sample database `client_data.db` into [main](../../main)

### Creating a TEQ account
  2. Click the button labeled `Create a New Account`.
  3. Fill in all the fields as required (different from the account created previously) and select the account type labeled `TEQ`, then click `Submit`.

### Log into the TEQ account and looking at the predictive analysis for Clients attending services
  4. Click the `Login` button and log into the TEQ account you created and click `Login` again.
  5. You will be greeted with a message asking "Hello x. What would you like to do?"
  6. Click on `Generate Reports`
  7. Click on `Predictive Analysis`
  8. There should be 5 tick boxes, and two dropdown fields. The tick boxes are any models that a user would like to see, and the dropdown fields are the month and year (default of today's month/year)
  9. Just simply clicking `Submit` should only provide a graph from the data from the database
  10. Clicking the `NaiveModel` tick box and then clicking submit should provde a graph from the database and a line that's elastic
  11. Clicking the `LinearRegression` tick box and then clicking submit should provide a graph from the database and a linear regression model
  13. Going back to the application, it should provide the linear regression model, where x is the start date of the database (starting at 1) and y is the frequency for a specified month-conversion
  14. Clicking on either `ExponentialSmoothing` models should produce a line graph that is sinusoidal, this graph has its limits and can only predict the next outcome
  15. For any of the models, the MAPE estimate value should appear
