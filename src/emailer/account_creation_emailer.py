import sendgrid
import os
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
        sg = sendgrid.SendGridAPIClient('SG.ME6PqRvVQeqs71zjlyHzCQ.cTKpy39V' +
                                        'LjkY52e8SMQTMyMyqfUiqdzHaZGsEPq1VTk')
        from_email = Email(self.email)
        to_email = Email(recipient)
        subject = "Email Verification"
        content = Content("text/plain", "This email is to notify you that " +
                          "your account has been successfully created.")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
