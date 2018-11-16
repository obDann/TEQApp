import sendgrid
import os
import sys
from sendgrid.helpers.mail import *
from emailer import Emailer

class AccountCreationEmailer(Emailer):

    def __init__(self):
        '''
        (AccountCreationEmailer, str) -> None
        
        Initialize AccountCreationEmailer
        '''
        self.email = "teqapp.noreply@gmail.com"

    def send(self, recipient):
        '''
        (Emailer, str) -> None
        
        Sends an email to the corresponding recipient about their account
        creation
        '''
        # check if recipient email is in database?, and if so then

        sg = sendgrid.SendGridAPIClient('SG.ME6PqRvVQeqs71zjlyHzCQ.cTKpy39VLj'
                                        + 'kY52e8SMQTMyMyqfUiqdzHaZGsEPq1VTk')
        from_email = Email(self.email)
        to_email = Email(recipient)
        subject = "Email Verification"
        # allow user to verify email by clicking a link?
        content = Content("text/plain", "This email is to notify you that " +
        "your account has been successfully created.")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
