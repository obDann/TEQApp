import pandas as pd

class DateQuantifier():
    '''
    A simple class that helps out with quantifying dates
    '''
    MONTHS_NAME = {"January": 1, "February": 2, "March": 3, "April": 4,
                   "May": 5, "June": 6, "July": 7, "August": 8,
                   "September": 9, "October": 10, "November": 11,
                   "December": 12}
    MONTHS_NUM = {1: "January", 2: "February", 3: "March", 4: "April",
                  5: "May", 6: "June", 7: "July", 8: "August",
                  9: "September", 10: "October", 11: "November",
                  12: "December"}

    def __init__(self, df):
        '''
        (DateQunatifier, DataFrame) -> None

        Initializes the date quantifier, assuming the DataFrame has a column
        "Year" and a column "Month"
        '''
        self._df = df

    def quantify_dates(self):
        '''
        (DateQuantifier) -> DataFrame

        Returns a dataframe that goes from the oldest time to the most recent
        time
        '''
        # what we want is the smallest and largest years
        young_month, young_year = self.get_youngest_date()
        old_month, old_year = self.get_oldest_date()
        # quantify the old and young
        young_year = int(young_year)
        old_year = int(old_year)

        # then we want to have a count, 12 * the differnce of the years
        count = 12 * (young_year - old_year)
        # in addition, the difference of the two months
        count += self.MONTHS_NAME[young_month] - self.MONTHS_NAME[old_month]
        count += 1

        # now we can populate our dataframe with the amount of months in
        # between
        the_data = {"x axis": [i for i in range(1, count+1)],
                    "Frequency": [0 for i in range(count)]}
        the_df = pd.DataFrame(the_data)
        # we now want the incrementing series
        month_s, year_s = self.get_increm_series(count, old_year,
                                                 self.MONTHS_NAME[old_month])
        the_df.loc[:, "Month"] = pd.Series(month_s)
        the_df.loc[:, "Year"] = pd.Series(year_s)


        return self.populate_frequencies(the_df)


    def populate_frequencies(self, new_df):
        '''
        (DateQuantifier, DataFrame) -> DataFrame

        Populates the frequencies in the dataframe
        '''
        index = 0
        # go through the years
        years = list(self._df.groupby("Year").count().index.values)

        for year in years:
            df = self._df[self._df["Year"] == str(year)]
            df = df.groupby("Month").count()["Year"]
            # get the months for that year
            months_for_year = list(df.index.values)
            for month in months_for_year:
                # hunt the index of that dataframe
                hunter = new_df[new_df["Month"] == month]
                hunter = hunter[hunter["Year"] == str(year)]
                index_val = int(hunter.index.values[0])
                # so at the index, and frequency, insert the month's frequency
                new_df.at[index_val, "Frequency"] = df[month]
        return new_df


    def get_increm_series(self, count, old_year, old_month):
        '''
         (DateQuantifier, int, int, int) -> [list of str], [list of str]

        Returns a two lists that sequentially spans from the
        oldest date to the youngest date
        '''
        # have our months and years list
        months = []
        years = []
        curr_val = old_month
        cur_year = old_year

        for i in range(count):
            cur_month_val = curr_val
            if (curr_val == 13):
                cur_month_val = 1
                curr_val = 1
                cur_year += 1
            # append the current month to months
            months.append(self.MONTHS_NUM[cur_month_val])
            # get the current year
            str_year = str(cur_year)
            # append year to year
            years.append(str_year)
            # increment curr value
            curr_val += 1
        # then return the two
        return months, years


    def get_oldest_date(self):
        '''
        (DateQuantifier) -> String, String

        Returns the oldest date
        '''
        years = list(pd.to_numeric(self._df["Year"]))
        oldest_year = min(years)
        # then we want to get the dataframe of the oldest year
        oldest_df = self._df[self._df["Year"] == str(oldest_year)]
        # next we want the list of months
        months = oldest_df.groupby("Month").count()
        months = list(months.index.values)
        # we want the minimum month
        quant = [self.MONTHS_NAME[month] for month in months]
        min_month = min(quant)
        return self.MONTHS_NUM[min_month], str(oldest_year)

    def get_youngest_date(self):
        '''
        (DateQuantifier) -> String, String

        Returns the most recent date in the dataframe
        '''
        years = list(pd.to_numeric(self._df["Year"]))
        young_year = max(years)
        # then we want to get the dataframe of the oldest year
        young_df = self._df[self._df["Year"] == str(young_year)]
        # next we want the list of months
        months = young_df.groupby("Month").count()
        months = list(months.index.values)
        # we want the minimum month
        quant = [self.MONTHS_NAME[month] for month in months]
        min_month = max(quant)
        return self.MONTHS_NUM[min_month], str(young_year)
