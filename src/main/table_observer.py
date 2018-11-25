import tkinter as tk
from tkinter import *
from Observer import Observer
import pandas as pd
import sys
sys.path.append("../commands")
import missing_val_checker as mv
import data_aggregator as da

class TableObserver(Observer):
    '''
    Observer object for button that allows users to upload excel files
    '''
        
    def __init__(self, data_frame, temp_name):
        ''' (UploadObserver) -> None
        
        Initializes an UploadObserver object
        '''
        self.df = data_frame
        self.template_name = temp_name
        
        
    def notify(self, obs):
        pass