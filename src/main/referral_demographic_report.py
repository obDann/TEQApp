import numpy as np
import matplotlib.pyplot as plt
import ReportAbstract

class ReferralDemographicReport(ReportAbstract):
    def __init__(self, title, x_label, y_label):
            ''' (ReportAbstract, str, str, str) -> None
            
            Initialize a report
            Sets the title and axis labels
            These persist after a  display
            '''
            fig, ax = plt.subplots()
            self.title = title
            self.x_label = x_label
            self.y_label = y_label            
    
    def add_data(self):
        ''' (ReportAbstract) -> None
        Adds a dataset to the Report
        After a display, all data must be readded
        '''
        pass
