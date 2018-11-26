import sendgrid
import os
import sys
from sendgrid.helpers.mail import *
from emailer import Emailer
import random
import client_db_functions


class PasswordForgettingEmailer(Emailer):

    def __init__(self):
        '''
        (PasswordForgettingEmailer, str) -> None

        Initialize PasswordForgettingEmailer
        '''
        self.email = "teqapp.noreply@gmail.com"

    def send(self, recipient):
        '''
        (Emailer, str) -> None

        Sends an email to the corresponding recipient about their current
        password.
        '''
        temp_pass = self.create_temp_pass()
        names = client_db_functions.get_username(recipient)
        client_db_functions.insert_temp_pass(str(names[0]), temp_pass)

        sg = sendgrid.SendGridAPIClient('SG.ME6PqRvVQeqs71zjlyHzCQ.cTKpy39V' +
                                        'LjkY52e8SMQTMyMyqfUiqdzHaZGsEPq1VTk')
        from_email = Email(self.email)
        to_email = Email(recipient)
        subject = "Forgotten Password"
        content = Content("text/plain", "Hello " + str(names[1]) + 
                          ", \n\nAs you have forgotten your password" +
                          ", use this temporary 6 digit passcode in order to" +
                          " log in so that you may change your password " +
                          "immediately afterward: \n" + temp_pass)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())

    def create_temp_pass(self):
        '''
        (Emailer) -> str

        Crafting a temporary password to be used and storing it into the
        database.
        '''
        temp_pass = ''
        for x in range(6):
            temp_pass += str(random.randint(0,9))
        return temp_pass
