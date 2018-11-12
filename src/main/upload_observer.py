import tkinter as tk
from tkinter import *
from Observer import Observer
import sys
sys.path.append("../commands")
import file_system_fetcher as fsf

class UploadObserver(Observer):
    '''
    '''
    
    def __init__(self):
        ''' (UploadObserver) -> None
        
        Initializes an UploadObserver object
        '''

    def notify(self, obs):
        '''
        (UploadObserver) -> None

        Uploads a file to the database according to a specified template name
        '''
        # make a template handler

        # make another root
        temp_root = Tk()
        # inject the root into the FileSystemFetcher
        my_fsf = fsf.FileSystemFetcher(temp_root)
        the_dataframe = my_fsf.execute()
        temp_root.mainloop()
        print(the_dataframe)
