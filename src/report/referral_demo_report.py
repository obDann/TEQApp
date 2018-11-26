import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("../graphs")
from histogram import Histogram

sys.path.append("../reports")
from database_retriever import * 

class ReferralDemoReport():
    '''
    Displays all the number of people in each different referral services.
    '''
    
    def __init__(self):
        # Variables for the graph
        ranging_variable = "Services"
        frequency = "People Count"
        report_name = "Different Referral Services"
        # Get the dataframe from query
        df = self.get_data(ranging_variable, frequency)
        
        # Create graph and display
        his = Histogram(df, ranging_variable, frequency, title= report_name)
        his.display()
    
    def get_data(x, y):
        '''
        Gets the data from query
        '''
        data = test()
        df = pd.DataFrame(data, columns=[x], index = [y])
        return df
    
if __name__ == "__main__":
    #a = ReferralDemoReport()
    b = ReferralAgeReport()