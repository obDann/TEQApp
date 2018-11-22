import tkinter as tk
from tkinter import *
from Observer import Observer
import sys
sys.path.append("../commands")
import file_system_fetcher as fsf
from screener import *
from duplicate_row_checker import *
from data_aggregator import *
sys.path.append("../temhelp")
from true_tem_handler import *


class UploadObserver(Observer):
    '''
    Observer object for button that allows users to upload excel files
    '''
    THE_COMMANDS = ["FileSystemFetcher", "DuplicateRowChecker", "Screener"]

    def __init__(self, parent, controller):
        ''' (UploadObserver, Tk, Frame) -> None

        Initializes an UploadObserver object
        '''
        self._parent = parent
        self._controller = controller

    def notify(self, obs):
        '''
        (UploadObserver) -> None

        Uploads a file to the database according to a specified template name
        '''


        template_name = obs.button.template


        # create a file system fetcher
        my_fsf = fsf.FileSystemFetcher(self._controller)
        # get the dataframe
        df = my_fsf.execute()

        # check if the fsf executed properly
        if (my_fsf.executed_properly()):
            self._run_screener(df, template_name)
        else:
            # if the user clicked 'x' in any of the frames in fsf
            # get the message
            the_opq = my_fsf.get_output_queue()
            the_msg = ''
            while not the_opq.is_empty():
                the_msg += the_opq.dequeue() + "\n"
            # make a small pop up
            mini_pop = tk.Tk()
            # make a label
            my_label = tk.Label(mini_pop, text=the_msg)
            my_label.pack()
            # make a button
            my_button = tk.Button(mini_pop, text="OK",
                                  command=mini_pop.destroy)
            my_button.pack()
            self._controller.deiconify()

            mini_pop.mainloop()

    def _run_screener(self, df, template_name):
        my_tth = TrueTemplateHandler(template_name)
        my_screener = Screener(df, my_tth)
        the_df = my_screener.execute()

        if (my_screener.executed_properly()):
            self._run_duplicate_row_checker(the_df, template_name)


    def _run_duplicate_row_checker(self, df, template_name):
        my_drc = DuplicateRowChecker(df)
        the_df = my_drc.execute()
        self._run_data_aggregator(df, template_name)


    def _run_data_aggregator(self, df, template_name):

        my_data_agg = DataAggregator(template_name)

        # get a template handler
        my_tth = TrueTemplateHandler(template_name)

        new_df = my_data_agg.execute(df, my_tth)
        print("I am here!!!")

        f = open("my_file.txt", "a")
        f.write("========================================")
        f.write(str(new_df))
        f.close()

