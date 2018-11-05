import sendgrid
import os
from sendgrid.helpers.mail import *
from emailer import Emailer

class PasswordForgettingEmailer(Emailer):

    def __init__(self, email):
        '''
        (PasswordForgettingEmailer, str) -> None
        
        Initialize PasswordForgettingEmailer
        '''
        self.email = email

    def send(self, recipient):
        '''
        (Emailer, str) -> None
        
        Sends an email to the corresponding recipient about their current
        password.
        '''
        # check if email is in database?, and if so then
        # self._exec_status = True
        # otherwise
        sg = sendgrid.SendGridAPIClient('SG.ME6PqRvVQeqs71zjlyHzCQ.cTKpy39VLj\
        kY52e8SMQTMyMyqfUiqdzHaZGsEPq1VTk')
        from_email = Email("teqapp.noreply@gmail.com")
        to_email = Email(recipient)
        subject = "Forgot your password"
        # allow user to reset their password? or show in email ??
        content = Content("text/plain", "Change your password")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())        

    def sent_properly(self):
        '''
        (Emailer) -> boolean

        Returns a boolean to determine whether the email could be sent or not
        '''
        return self._exec_status
