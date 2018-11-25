import pandas as pd
from command import Command
from tkinter import *
import datetime


class DateAsker(Command):
    MONTHS = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
              6: "June", 7: "July", 8: "August", 9: "September",
              10: "October", 11: "November", 12: "December"}

    def __init__(self, tk_root):
        '''
        (DateAsker, Tk) -> None

        Initialize the DateAsker; asks user for a date they would like to
        upload for
        '''
        # Initialize an output queue and status
        Command.__init__(self)
        # What we want to do is to make a top level so that we can pop up
        self._toplevel = Toplevel(tk_root)
        todays_year = int(datetime.datetime.today().strftime('%Y'))
        todays_month = int(datetime.datetime.today().strftime('%m'))
        # what we would like to do now is to set a default month and year
        default_year = str(todays_year)
        default_month = self.MONTHS[todays_month]
        # and we want a dropdown, so we make a couple string vars
        self._default_year = StringVar()
        self._default_month = StringVar()
        self._default_year.set(default_year)
        self._default_month.set(default_month)
        # now we want to generate a range for dropdown values
        self._dropdown_year = [i for i in range(todays_year, 1950, -1)]
        self._dropdown_month = list(self.MONTHS.values())
        # create defaults prior to submit
        self._submit_flag = False
        self._submit_month = ''
        self._submit_year = ''
        # now run selection
        self._run_selection()

    def execute(self):
        '''
        (DateAsker) -> (str, str)

        Returns a tuple representing the month and the year.

        If a date is not selected, then this method returns None, and its
        output queue is populated
        '''
        # wait for our top level to be truely destroyed
        self._toplevel.wait_window()

        # then we have to check whether or not the user did click submit
        if self._submit_flag:
            # if the user did click submit, then we can return the month and
            # year
            # don't forget about setting our execution status
            self._exec_status = True
            return self._submit_month, self._submit_year
        else:
            # otherwise, inform the user what happened
            self._opq.enqueue("No Date is selected. Please try again.")

    def executed_properly(self):
        '''
        (FileSystemFetcher) -> boolean

        Determines whether or not the FileSystemFetcher was executed
        properly
        '''
        return self._exec_status

    def _run_selection(self):
        '''
        (FileSystemFetcher) -> None

        Let's a user pick out a sheet
        '''
        # ask the user what date they would be uploading for
        my_text_label = "What date are you going to be uploading for?"
        label = Label(self._toplevel, text=my_text_label)
        label.pack()

        # then what is wanted is a dropdown option list
        month_menu = OptionMenu(self._toplevel, self._default_month,
                                *self._dropdown_month)
        month_menu.pack()

        # then what is wanted is a dropdown option list
        year_menu = OptionMenu(self._toplevel, self._default_year,
                               *self._dropdown_year)
        year_menu.pack()

        # then have a select button; once the user presses select, the
        # string is returned
        select_button = Button(self._toplevel, text="Select",
                               command=self._submit)
        select_button.pack()

    def _submit(self):
        '''
        (FileSystemFetcher) -> None

        Determines what happens after a user clicks submit
        '''
        # the person can now execute date asker
        self._submit_flag = True
        # set the name of the year and month
        self._submit_month = self._default_month.get()
        self._submit_year = self._default_year.get()
        # then destroy the top level
        self._toplevel.destroy()


if __name__ == '__main__':
    tk_root = Tk()
    tk_root.withdraw()
    my_fsf = DateAsker(tk_root)
    x = my_fsf.execute()
    print(x)
    tk_root.mainloop()
