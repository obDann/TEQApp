import sendgrid
import os
import sqlite3
import sys
sys.path.insert(0, "../database")
import database_methods
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
        #(conn, cur) = database_methods.connection('users.db')
        #query = ("SELECT Name, Type from User where Email = ?")
        #try:
            #cur.execute(query, recipient)
            #error = 0
        #except sqlite3.Error as e:
            #print(format(e))
            #error = 1

        #if (not(error)):
            #name = cur.fetchall()
            #if (len(name) != 0):
                #self._exec_status = True

        #if (not self._exec_status):
            #return None

        sg = sendgrid.SendGridAPIClient('SG.ME6PqRvVQeqs71zjlyHzCQ.cTKpy39VLj\
        kY52e8SMQTMyMyqfUiqdzHaZGsEPq1VTk')
        from_email = Email("teqapp.noreply@gmail.com")
        to_email = Email(recipient)
        subject = "Forgot your password?"
        # allow user to reset their password? or show in email ??
        content = Content("text/plain", "As you have forgotten your password,\
        use this temporary password in order to log in so that you may change\
        your password immediately afterward: \n")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())        
