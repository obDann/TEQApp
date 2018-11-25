from tkinter import *
sys.path.append("../main")
import reports_page as rp
from date_quantifier import *
from exponential_smoothing_model import *
from exponential_smoothing_trends_model import *
from linear_regression_model import *
from naive_model import *
import sqlite3 as sql
import importlib
import datetime
import matplotlib.pyplot as plt


class PredictPage():
    MODELS = ["ExponentialSmoothingModel", "ExponentialSmoothingTrendsModel",
              "LinearRegressionModel", "NaiveModel"]

    MONTHS_NUM = {1: "January", 2: "February", 3: "March", 4: "April",
                  5: "May", 6: "June", 7: "July", 8: "August",
                  9: "September", 10: "October", 11: "November",
                  12: "December"}
    MONTHS_NAME = {"January": 1, "February": 2, "March": 3, "April": 4,
                   "May": 5, "June": 6, "July": 7, "August": 8,
                   "September": 9, "October": 10, "November": 11,
                   "December": 12}

    def __init__(self, controller, name):
        '''
        (PredictPage, TEQApp, Tk, str) -> None

        Shows the predictive analysis page
        '''

        self.name = name
        self.cont = controller
        # tk.Frame.__init__(self,parent)
        self.ticks = {}

        label = Label(self.cont, text = "Which models would you like to see?")
        label.grid(column=1)

        row_iter = 1
        col_iter = 0
        # make int vars for check boxes for a specific model
        for model in self.MODELS:
            self.ticks[model] = IntVar()
            cb = Checkbutton(self.cont, text=model, variable=self.ticks[model])
            cb.grid(row=row_iter, column = col_iter, sticky=W)
            col_iter += 1
            if (col_iter == 3):
                col_iter = 0
                row_iter += 1

        # then we want to make a dropdown of future values, so we get today's
        # date

        # we want a list of years; let's put up until 2100 just for show
        todays_year = int(datetime.datetime.today().strftime('%Y'))
        year_list = [str(i) for i in range(todays_year, 2101)]
        # we want to have the months for a default value
        todays_month = int(datetime.datetime.today().strftime('%m'))
        months_list = [self.MONTHS_NUM[i] for i in range(1,13)]

        self._selected_month = StringVar()
        self._selected_month.set(self.MONTHS_NUM[todays_month])

        self._selected_year = StringVar()
        self._selected_year.set(todays_year)

        # then we want to add a dropdown
        another_label = Label(self.cont, text="What date to predict?")
        new_row = row_iter + 1
        another_label.grid(row=new_row, column=0)
        month_menu = OptionMenu(self.cont, self._selected_month, *months_list)
        month_menu.grid(row=new_row, column=1)
        year_menu = OptionMenu(self.cont, self._selected_year, *year_list)
        year_menu.grid(row=new_row, column=2)

        my_butt = Button(self.cont, text="Submit", command=self._on_submit)
        my_butt.grid(column=1)





        #back = Button(self, text="Back",
                            #command=lambda: controller.set_page(rp.ReportsPage,
                                                             #self.name))
        #back.pack(side=TOP,fill=X)

    def _on_submit(self):
        '''
        (PredictPage) -> None

        Shows the predictive analysis data to the user
        '''
        df = self._get_ideal_df()
        num_rows = df.shape[0]
        my_plot_list = []
        my_label_list = []

        # plot the data
        x = "x axis"
        base, = plt.plot(x, "Frequency", data=df, linestyle="-", marker='o')
        my_plot_list.append(base)
        my_label_list.append("Frequency")


        mape_vals = {}
        # we want to go through all of the models that were selected
        for model in self.ticks:
            the_iv = self.ticks[model].get()
            # check if the model is checked
            if the_iv:
                # use reflection to instantiate the model
                modu_name = self._get_mod_name(model)
                module = importlib.import_module(modu_name)
                the_model_ins = getattr(module, model)(df, "x axis",
                                                       "Frequency")
                # get the model
                the_model, col = the_model_ins.get_model()
                # get the mape of the model
                mape_vals[model] = the_model_ins.get_mape_estimate(the_model,
                                                                   col)
                # append the projected model's data into the df
                df.loc[:, model] = pd.Series(the_model[col].head(num_rows))
                # add that to our plot
                my_label = self._get_label(model)
                print(my_label)
                sm_plot, = plt.plot(x, model, data=df, linestyle="-",
                                    marker='o')
                my_plot_list.append(sm_plot)
                my_label_list.append(my_label)

        plt.legend(my_plot_list, my_label_list)
        plt.show()


    def _get_mod_name(self, model):
        '''
        (PredictPage, str) -> str

        Returns the string of the module that the model is in
        '''
        my_str = ''
        first_flag = True
        for letter in model:
            # check for the first letter
            if first_flag:
                my_str += letter.lower()
                first_flag = False
            # check if the letter has capitalization
            elif letter.isupper():
                my_str += "_" + letter.lower()
            else:
                my_str += letter
        return my_str

    def _get_label(self, model):
        '''
        (PredictPage, str) -> str

        Returns a string that is appropriate for the model
        '''
        my_str = ''
        first_flag = True
        for letter in model:
            # check for the first letter
            if first_flag:
                my_str += letter
                first_flag = False
            # check if the letter has capitalization
            elif letter.isupper():
                my_str += " " + letter
            else:
                my_str += letter
        return my_str


    def _get_ideal_df(self):
        '''
        (PredictPage) -> DataFrame

        Returns the ideal dataframe for this page
        '''
        og_df = self._get_df_from_db()
        # let's put it in our date quantifier
        date_q = DateQuantifier(og_df)

        # and let's get the "youngest" date and quantify it
        young_month, young_year = date_q.get_youngest_date()
        db_month = self.MONTHS_NAME[young_month]
        db_year = int(young_year)

        # get the submission
        sub_month = self.MONTHS_NAME[self._selected_month.get()]
        sub_year = int(self._selected_year.get())
        sub_l_month = self._selected_month.get()
        sub_l_year = self._selected_year.get()

        # if the selected month and year is less than our data, then we have to
        # expand our data
        count_between = (sub_year - db_year) * 12
        count_between += sub_month - db_month

        if (count_between > 0):
            # we would have to expand it
            # so we make another df
            appending_data = {"Month": [sub_l_month],
                              "Year": [sub_l_year]}
            append_df = pd.DataFrame(appending_data)
            og_df = og_df.append(append_df)
            # reset the index
            og_df.reset_index(drop=True)
            # now we can remake our date quantifier
            date_q = DateQuantifier(og_df)
            new_df = date_q.quantify_dates()
            # hunt the index of that dataframe
            hunter = new_df[new_df["Month"] == sub_l_month]
            hunter = hunter[hunter["Year"] == sub_l_year]
            index_val = int(hunter.index.values[0])
            # then reset the frequency of it to 0
            new_df.at[index_val, "Frequency"] = 0
            return new_df
        else:
            # so we can get our df
            our_df = date_q.quantify_dates()
            # hunt the index of that dataframe
            hunter = our_df[our_df["Month"] == sub_l_month]
            hunter = hunter[hunter["Year"] == sub_l_year]
            index_val = int(hunter.index.values[0])
            # then the new dataframe is until that time
            new_df = our_df.head(index_val + 1)
            return new_df

    def _get_df_from_db(self):
        '''
        (PredictPage) -> DataFrame

        Returns a DataFrame from the database that at least guarantees the
        label as "Month" and "Year"
        '''
        # what we want to do is to get the relative dataframe from the database
        # create a connector
        connector = sql.connect("../database/client_data.db")
        # create a cursor
        cur = connector.cursor()
        query = "SELECT *"
        query += "FROM Client_Attends_Service"
        df_result = pd.read_sql(query, connector)
        return df_result[["Month", "Year"]]

if __name__ == "__main__":
    my_root = Tk()
    my_root.title("yaho")
    predict_pg = PredictPage(my_root, "name")
    my_root.mainloop()