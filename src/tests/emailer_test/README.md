# AccountCreationEmailer and PasswordForgettingEmailer tests

The tests for these two emailers are essentially the same, but the contents of the email will differ. The purpose of these tests are to show that we can, in fact, receive an email when the object is created and a proper recipient is entered as input.

Traverse into the [emailer_test](.) folder in order to begin testing. The first step is to input in commandline `python3 base_code.py`. After this step, there is one type of test per emailer that can be conducted:

### Test 1: Sending an email with AccountCreationEmailer

After typing the line `python3 base_code.py`, follow the instructions presented by the python shell. It will first prompt you to enter your email. Note that this emailer will not check if you are entering a correct email address. Be sure you are entering the correct email address, otherwise you will not be able to check to see if you received the correct email.

After completing this step, you should check your email (check spam/junk folders as well) to see if you have received an email.
The email should look like this:

![alt text](https://github.com/CSCC01/Team10/blob/emailer/src/tests/emailer_test/pics/email_verification.png)

The result should have your own email instead of your@emailaddress.com.

### Test 2: Sending an email with PasswordForgettingEmailer

After typing the line `python3 base_code.py`, follow the instructions presented by the python shell. It will first prompt you to enter your email. Note that this emailer will not check if you are entering a correct email address. Be sure you are entering the correct email address, otherwise you will not be able to check to see if you received the correct email.

After completing this step, you should check your email (check spam/junk folders as well) to see if you have received an email.
The email should look like this:

![alt text](https://github.com/CSCC01/Team10/blob/emailer/src/tests/emailer_test/pics/forgotten_password.png)

The result should have your own email instead of your@emailaddress.com.
