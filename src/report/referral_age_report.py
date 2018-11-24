import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("../graphs")
from pie_graph import PieGraph

sys.path.append("../reports")
from database_retriever import * 

class ReferralAgeReport():
    '''
    Displays a pie graph of how the age groups are divided in a service
    '''
    def __init__(self):
        report_name = "Referral Age Report"
        label = "Age Groups"
        # X axis
        age_df = ["0-12","13-18","19-29","30-39","40-49","50-59","60-69",
                  "70-79","80-89","90+"]
        age_df = pd.DataFrame(age_df, columns=[label])
        
        # Y axis
        frequency = "People Count"
        count_df = get_age_groups()
        count_df = pd.DataFrame(count_df, columns=[frequency])
        
        # Merge the two columns
        df = pd.concat([age_df,count_df],axis=1)
        
        # Graph
        #pie = PieGraph(df, label, frequency, title=report_name)
   