import tkinter as tk
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


class PredictPage(tk.Frame):
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

    def __init__(self, parent, controller, name):
        '''
        (PredictPage, TEQApp, Tk, str) -> None

        Shows the predictive analysis page
        '''
        self.name = name
        self.cont = controller
        tk.Frame.__init__(self, parent)
        self.ticks = {}

        label = Label(self, text="Which models would you like to see?")
        label.grid(column=1)

        self._row_iter = 1
        self._col_iter = 0
        # make int vars for check boxes for a specific model
        for model in self.MODELS:
            self.ticks[model] = IntVar()
            cb = Checkbutton(self, text=model, variable=self.ticks[model])
            cb.grid(row=self._row_iter, column=self._col_iter, sticky=W)
            self._col_iter += 1
            if (self._col_iter == 3):
                self._col_iter = 0
                self._row_iter += 1

        # then we want to make a dropdown of future values, so we get today's
        # date

        # we want a list of years; let's put up until 2100 just for show
        todays_year = int(datetime.datetime.today().strftime('%Y'))
        year_list = [str(i) for i in range(todays_year, 2101)]
        # we want to have the months for a default value
        todays_month = int(datetime.datetime.today().strftime('%m'))
        months_list = [self.MONTHS_NUM[i] for i in range(1, 13)]

        self._selected_month = StringVar()
        self._selected_month.set(self.MONTHS_NUM[todays_month])

        self._selected_year = StringVar()
        self._selected_year.set(todays_year)

        # then we want to add a dropdown
        another_label = Label(self, text="What date to predict?")
        self._row_iter = self._row_iter + 1
        another_label.grid(row=self._row_iter, column=0)
        month_menu = OptionMenu(self, self._selected_month, *months_list)
        month_menu.grid(row=self._row_iter, column=1)
        year_menu = OptionMenu(self, self._selected_year, *year_list)
        year_menu.grid(row=self._row_iter, column=2)

        my_butt = Button(self, text="Submit", command=self._on_submit)
        my_butt.grid(column=1)

        back = Button(self,
                      text="Back",
                      command=lambda: self.cont.set_page(rp.ReportsPage,
                                                         self.name))
        back.grid(column=0)
        self._row_iter += 3

    def _on_submit(self):
        '''
        (PredictPage) -> None

        Shows the predictive analysis data to the user
        '''
        fig, ax = plt.subplots()
        df, orig_dat_pts = self._get_ideal_df()
        num_rows = df.shape[0]
        my_plot_list = []
        my_label_list = []
        reg_details = [None, None]
        exp_smooth = {}
        opt_alpha = None
        opt_ab = [None, None]

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
                # one odd case is if the model is linear
                if (model == "LinearRegressionModel"):
                    the_model_i = getattr(module, model)(df.head(orig_dat_pts),
                                                         "x axis", "Frequency")
                    temp = the_model_i.get_details()
                    reg_details[0], reg_details[1] = temp[0], temp[1]
                    temp_srs = df["x axis"] * reg_details[0] + reg_details[1]
                    df.loc[:, model] = temp_srs
                    # get the mape of the model
                    mape_vals[model] = the_model_i.get_mape_estimate()
                else:
                    if num_rows < orig_dat_pts:
                        df_rep = df.head(num_rows)
                        the_model_i = getattr(module, model)(df_rep, "x axis",
                                                             "Frequency")
                        # get the model
                        the_model, col = the_model_i.get_model()
                        # append the projected model's data into the df
                        temp = pd.Series(the_model[col].head(num_rows))
                        df.loc[:, model] = temp
                        if model.startswith("Expo"):
                            # we want the next projected upload
                            exp_smooth[model] = the_model[col].iloc[num_rows]
                    else:
                        df_rep = df.head(orig_dat_pts)
                        the_model_i = getattr(module, model)(df_rep, "x axis",
                                                             "Frequency")
                        # get the model
                        the_model, col = the_model_i.get_model()
                        # append the projected model's data into the df
                        temp = pd.Series(the_model[col].head(orig_dat_pts))
                        df.loc[:, model] = temp
                        # check if the model starts with exponential smoothing
                        if model.startswith("Expo"):
                            # we want the next projected upload
                            o = orig_dat_pts
                            exp_smooth[model] = the_model[col].iloc[o]

                # get the mape of the model
                mape_vals[model] = the_model_i.get_mape_estimate()

                if (model == "ExponentialSmoothingModel"):
                    opt_alpha = the_model_i.get_optimal_alpha()
                elif (model == "ExponentialSmoothingTrendsModel"):
                    clone = the_model_i
                    opt_ab[0], opt_ab[1] = clone.get_optimal_alpha_and_beta()

                # add that to our plot
                my_label = self._get_label(model)
                sm_plot, = plt.plot(x, model, data=df, linestyle="-",
                                    marker='o')
                my_plot_list.append(sm_plot)
                my_label_list.append(my_label)

        if (bool(mape_vals)):
            msg = "-------------------------------"
            Label(self, text=msg).grid(row=self._row_iter, column=0, sticky=E)
            Label(self, text=msg).grid(row=self._row_iter, column=1, sticky=W)
            self._row_iter += 1

        if (bool(exp_smooth)):
            msg = "Next projected estimate for:"
            Label(self, text=msg).grid(row=self._row_iter,
                                                         column=0,
                                                         sticky=W)
            self._row_iter += 1
            for key in exp_smooth:
                Label(self, text=key).grid(row=self._row_iter, column=0,
                                           sticky=E)
                Label(self, text=str(exp_smooth[key])).grid(row=self._row_iter,
                                                            column=1,
                                                            sticky=W)
                self._row_iter += 1

        if opt_alpha is not None:
            msg = "Optimality:"
            Label(self, text=msg).grid(row=self._row_iter,
                                                         column=0,
                                                         sticky=W)
            self._row_iter += 1
            msg = "Optimal alpha for Exponential Non Trends Model:"
            Label(self, text=msg).grid(row=self._row_iter, column=0,
                                       sticky=E)
            Label(self, text=str(opt_alpha)).grid(row=self._row_iter,
                                                 column=1, sticky=W)
            self._row_iter += 1

        if opt_ab[0] is not None:
            msg = "Optimality:"
            Label(self, text=msg).grid(row=self._row_iter,
                                                         column=0,
                                                         sticky=W)
            self._row_iter += 1
            msg_1 = "Optimal alpha with Trends Model:"
            msg_2 = "Optimal beta with Trends Model:"
            Label(self, text=msg_1).grid(row=self._row_iter, column=0,
                                         sticky=E)
            Label(self, text=str(opt_ab[0])).grid(row=self._row_iter, column=1,
                                                 sticky=W)
            self._row_iter += 1
            Label(self, text=msg_2).grid(row=self._row_iter, column=0,
                                         sticky=E)
            Label(self, text=str(opt_ab[1])).grid(row=self._row_iter, column=1,
                                                  sticky=W)
            self._row_iter += 1
        # check if the linear regression model is ran
        if reg_details[0] is not None:
            # if it is ran, then we want to provide the details
            lm = "y = " + str(reg_details[0])
            lm += "x + " + str(reg_details[1])
            some_label = Label(self, text="Linear Model:")
            some_label.grid(row=self._row_iter, column=0, sticky=E)
            another_la = Label(self, text=lm)
            another_la.grid(row=self._row_iter, column=1, sticky=W)
            self._row_iter += 1

        if (bool(mape_vals)):
            Label(self, text="MAPE:").grid(row=self._row_iter,
                                           column=0, sticky=W)
            self._row_iter += 1

        # go through the MAPE
        for key in mape_vals:
            la = Label(self, text=key)
            la.grid(row=self._row_iter, column=0, sticky=E)
            nla = Label(self, text=str(mape_vals[key]))
            nla.grid(row=self._row_iter, column=1, sticky=W)
            self._row_iter += 1

        months = [""] + list(df["Month"])
        years = [""] + list(df["Year"])
        x_axis = [months[i] + " " + years[i] for i in range(len(months))]
        x_count = [i for i in range(len(x_axis))]
        plt.xticks(x_count, x_axis)
        plt.title("People Attending Services over time")
        plt.xlabel("Months-Years")
        plt.ylabel("Number of people attending services")
        plt.xticks(rotation=90)
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
        (PredictPage) -> DataFrame, int

        Returns the ideal dataframe for this page and number of least number of
        data points from the database
        '''
        og_df = self._get_df_from_db()
        # let's put it in our date quantifier
        date_q = DateQuantifier(og_df)
        # quantify the dates so that we can get the number of original data
        # points
        num_data_pts_temp = date_q.quantify_dates()
        num_data_pts = num_data_pts_temp.shape[0]

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
            return new_df, num_data_pts
        else:
            # so we can get our df
            our_df = date_q.quantify_dates()
            # hunt the index of that dataframe
            hunter = our_df[our_df["Month"] == sub_l_month]
            hunter = hunter[hunter["Year"] == sub_l_year]
            index_val = int(hunter.index.values[0])
            # then the new dataframe is until that time
            new_df = our_df.head(index_val + 1)
            return new_df, new_df.shape[0]

    def _get_df_from_db(self):
        '''
        (PredictPage) -> DataFrame

        Returns a DataFrame from the database that at least guarantees the
        label as "Month" and "Year"
        '''
        # what we want to do is to get the relative dataframe from the database
        # create a connector
        connector = sql.connect("../main/client_data.db")
        # create a cursor
        cur = connector.cursor()
        query = "SELECT *"
        query += "FROM Client_Attends_Service"
        df_result = pd.read_sql(query, connector)
        return df_result[["Month", "Year"]]
