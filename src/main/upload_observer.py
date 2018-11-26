import tkinter as tk
from tkinter import *
from Observer import Observer
import sys
from data_viewer_page import *
sys.path.append("../commands")
from file_system_fetcher import *
from screener import *
from duplicate_row_checker import *
from data_aggregator import *
from date_asker import *
sys.path.append("../temhelp")
from true_tem_handler import *


class UploadObserver(Observer):
    '''
    Observer object for button that allows users to upload excel files
    '''
    THE_DF_COMMANDS = ["FileSystemFetcher", "Screener", "DuplicateRowChecker"]

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
        self._can_continue = True
        # general initialization before processing
        template_name = obs.button.template
        user_name = obs.button.name
        df = None

        # we want to continue while the commands execute properly, so we make
        # and index
        index = 0
        while (index < len(self.THE_DF_COMMANDS) and self._can_continue):
            the_command = self.THE_DF_COMMANDS[index]
            # get the reflection string
            reflect_string = self._get_reflection_string(the_command)
            # we want to pass in a dataframe and the template name
            # by reflection
            df = getattr(self, reflect_string)(df, template_name)
            index += 1

        # and now we want the month and year the person is uploading for, but
        # we also have to check if we can still could continue
        if (self._can_continue):
            the_date_tuple = self._run_date_asker()
            # then check if we can still continue...
            if (self._can_continue):
                month = the_date_tuple[0]
                year = the_date_tuple[1]
                # then we can pass the DataFrame and the month and year
                self._controller.insert_page_details(DataViewerPage,
                                                     df, template_name,
                                                     month, year,
                                                     user_name)

    def _get_reflection_string(self, the_str):
        '''
        (UploadObserver, str) -> str

        Returns a string representation of a method in the upload observer
        '''
        my_str = "_run"

        for letter in the_str:
            # check if the letter is uppercase
            if (letter.isupper()):
                # if it is, prepend an underscore
                my_str += "_" + letter.lower()
            else:
                my_str += letter
        return my_str

    def _run_file_system_fetcher(self, df, template_name):
        '''
        (UploadObserver, DataFrame, str) -> DataFrame

        Runs the file system fetcher and withdraws the root
        '''
        # instantiate the file system fetcher
        my_fsf = FileSystemFetcher(self._controller)
        # execute the file system fetcher
        df = my_fsf.execute()
        # check the execution status
        if (my_fsf.executed_properly()):
            # if it executed properly, then we can return the dataframe
            return df
        else:
            self._bad_execution(my_fsf)

    def _run_screener(self, df, template_name):
        '''
        (UploadObserver, DataFrame, str) -> DataFrame

        Runs the Screener to ensure the dataframe corresponds to the passed
        template name
        '''
        # make a true template handler
        my_tth = TrueTemplateHandler(template_name)
        # instantiate a screener
        my_screener = Screener(df, my_tth)
        # get the dataframe
        df = my_screener.execute()

        if (my_screener.executed_properly()):
            # if it execute properly, return the dataframe
            return df
        else:
            # otherwise its bad on execution
            self._bad_execution(my_screener)

    def _run_duplicate_row_checker(self, df, template_name):
        '''
        (UploadObserver, DataFrame, str) -> DataFrame

        Removes duplicate rows
        '''
        my_drc = DuplicateRowChecker(df)
        the_df = my_drc.execute()

        if (my_drc.executed_properly()):
            return the_df
        else:
            self._bad_execution(my_screener)

    def _run_date_asker(self):
        '''
        (UploadObserver) -> tuple of (str, str)

        Returns the month and date the user wants to upload for
        '''
        my_da = DateAsker(self._controller)
        date_tuple = my_da.execute()

        if (my_da.executed_properly()):
            return date_tuple
        else:
            self._bad_execution(my_screener)

    def _bad_execution(self, cmd):
        '''
        (UploadObserver, Command) -> None

        Informs the user what happened on a bad execution and deiconifies
        the root
        '''
        # we cannot continue to execute things anymore
        self._can_continue = False
        # get the command's output queue
        the_opq = cmd.get_output_queue()
        the_msg = ''
        # generate a message based on the output queue
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
