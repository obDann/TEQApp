import tkinter as tk
import csv
import sqlite3
from tkinter import *
from Observer import Observer
from random import randint


class CustomQueryObserver(Observer):
    '''
    Observer object for button that allows users to save query data into
    csv files.
    '''
        
    def __init__(self):
        ''' (UploadObserver) -> None
        
        Initializes an CustomQueryObserver object
        '''
        
        
    def notify(self, obs):
        '''
        Saves the data into an csv file.
        '''
        temp_num = str(randint(1, 9999))
        # Establish a sqlite connection
        conn = sqlite3.connect('client_data.db')
        cur = conn.cursor()
        try:
            # Get the user query
            query = self.retrieve_input()
            cur.execute(query)
            result = cur.fetchall()
            # Write the result into a csv file
            with open('csvfile' + temp_num +'.csv', "w", newline='') as csv_file: 
                writer = csv.writer(csv_file, delimiter=',')
                for line in result:
                    writer.writerow(line)                
        except TypeError as e:
            print("Invalid SQL input, with the message: " + e)
            # Finish message
        print("Finished executing query.")        