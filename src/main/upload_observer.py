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

        # check if the file system fetcher executed properly
        if (my_fsf.executed_properly()):
            # we are going to be appropriately setting the headers. The
            # headers are typically on the third row. The title is in the
            # 1st row, so the headers are actually on the 3rd row.
            header = the_dataframe.iloc[1]
            # cut the rest of the dataframe
            the_dataframe = the_dataframe[2:]
            # and then rename the headers
            the_dataframe = the_dataframe.rename(columns = header)
            print(the_dataframe)
