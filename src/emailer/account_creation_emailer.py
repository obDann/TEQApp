import sendgrid
import os
from sendgrid.helpers.mail import *
from emailer import Emailer

# for sending emails through python
import smtplib
# importing email module
from email.mime.text import MIMEText

class AccountCreationEmailer(Emailer):

    def __init__(self, email):
        '''
        (AccountCreationEmailer, str) -> None
        
        Initialize AccountCreationEmailer
        '''
        self.email = email

    def send(self, recipient):
        '''
        (Emailer, str) -> None
        
        Sends an email to the corresponding recipient about their account
        creation
        '''
        sg = sendgrid.SendGridAPIClient('SG.ME6PqRvVQeqs71zjlyHzCQ.cTKpy39VLj\
        kY52e8SMQTMyMyqfUiqdzHaZGsEPq1VTk')
        from_email = Email("teqapp.noreply@gmail.com")
        # check if email is in database?
        to_email = Email(recipient)
        subject = "Email Verification"
        # allow user to verify email by clicking a link?
        content = Content("text/plain", "This email is to notify you that \
        your account has been successfully created")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())        

    def sent_properly(self):
        '''
        (Emailer) -> boolean

        Returns a boolean to determine whether the email could be sent or not
        '''
