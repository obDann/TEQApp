# FileSystemFetcher Tests

Assuming you are int hte [file_system_fetcher_test](.) folder, there are several tests that can be conducted. The first step is to input in commandline `Python3 base_code.py`. Following this step, there are approximately 3 different tests:

### Test 1: An excel file with a single sheet

After typing `Python3 base_code.py`, navigate to the [file_system_fetcher_test](.) folder and click on "test.xlsx". If you are able to open this file, notice that this file only has one sheet. Once you click on "test.xlsx", then the "Open" button:



The Python shell will output data as it is in the excel file:


### Test 2: An excel file with more than one sheet (confirming the data of the right sheet)

After typing `Python3 base_code.py`, navigate to the [file_system_fetcher_test](.) folder and click on "test2sheets.xlsx". If you are able to open this file, notice that this file has two sheets.

Once you click on "test2sheets.xlsx" and then the "Open" button, you will find a window popping up, asking what sheet you would like to choose. Click on your preferred sheet and then "Submit":


The expected output for "Sheet1" should look like:



The expected output for "Sheet2" should look like:



### Test 3: Prematurely exiting out of the FileSystemFetcher

After typing `Python3 base_code.py`, the file system window should pop up. Close it. By exiting it, it would mean that our the file system fetcher has not successfully been executed. Since we have initialized the FileSystemFetcher as the variable `my_fsf` in the base code, you can check its status by doing `my_fsf.executed_properly()`. It is expected that the output is `False`.
