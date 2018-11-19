import tkinter as tk
from tkinter import *
from Observer import Observer
import sys
sys.path.append("../commands")
import file_system_fetcher as fsf
from screener import *
sys.path.append("../temhelp")
from true_tem_handler import *


class UploadObserver(Observer):
    '''
    Observer object for button that allows users to upload excel files
    '''

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
            self._after_fsf(df, template_name)
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


    def _after_fsf(self, df, template_name):
        my_tth = TrueTemplateHandler(template_name)
        my_screener = Screener(df, my_tth)
        my_screener.execute()
        if (my_screener.executed_properly()):
            self._after_screener(df)
        else:
            self._checker()
        print("hello world")


    def _after_screener(self, df):
        print(df)


    def _checker(self):
        print("a linked list of functions")