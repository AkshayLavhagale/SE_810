""" Akshay Lavhagale
    Homework 08
    Practice and learn Date Arithmetic Operations, field separated file reader and Scanning directories and files """


import datetime
import os
from prettytable import PrettyTable


# Part 1: date_arithmetic Date Arithmetic Operations
def date_arithmetic():
    """ Write a function date_arithmetic to use Python’s datetime module """

    num_days = 3
    date5 = "27 Feb 2000"
    date6 = "27 Feb 2017"
    dt5 = datetime.datetime.strptime(date5, "%d %b %Y")
    dt6 = datetime.datetime.strptime(date6, "%d %b %Y")
    dt3 = dt5 + datetime.timedelta(days=num_days)
    dt7 = dt6 + datetime.timedelta(days=num_days)
    three_days_after_02272000 = f"{num_days} days after {dt5:%m/%d/%Y} is {dt3:%m/%d/%Y}"
    three_days_after_02272017 = f"{num_days} days after {dt6:%m/%d/%Y} is {dt7:%m/%d/%Y}"

    date1 = "01 Jan 2017"
    date2 = "27 Oct 2017"
    dt1 = datetime.datetime.strptime(date1, "%d %b %Y")
    dt2 = datetime.datetime.strptime(date2, "%d %b %Y")
    order = 'before' if dt1 < dt2 else 'after'
    delta = dt2 - dt1
    days_passed_01012017_10312017 = f"{dt1:%m/%d/%Y} occurs {delta.days} days {order} {dt2:%m/%d/%Y}"

    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017


# Part 2: file_reading_gen field separated file reader
def file_reading_gen(path, fields, sep='|', header=False):
    """ Generator function file_reading_gen to read field-separated text files and yield a tuple with all of the values
        from a single line in the file on each call to next() """
    try:
        file = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f'File {path} cannot be opened.')  # explain the reason why this happened
    else:
        with file:  # it will close the file on its own. If exception is occured in between it will not close and for that with require.
            for count_1, line in enumerate(file):
                line = line.rstrip('\n')
                tokens = line.split(sep)   # fields = line.rstrip('\n').split(sep)
                if fields != len(tokens):  # get comfortable with debugger
                    raise ValueError(f'{os.path.basename(path)} has {len(tokens)} fields on line {count_1}'
                                     f'but expected {fields}')
                elif header and count_1 == 0:
                    continue  # skipping the header after checking for correct number of fields
                else:
                    yield tuple(tokens)


class FileAnalyzer:
    """ For each .py file, open each file and calculate a summary of the file """
    def __init__(self, directory):

        self.directory = directory

        self.files_summary = dict()

        self.analyze_files()  # summarize the python files data
# make a habit of providing what represents keys and values in dictionary.

    def analyze_files(self):
        """ Python dictionary that store the summarized data for the given file path """
        try:
            files = os.listdir(self.directory)
        except FileNotFoundError:
            raise FileNotFoundError(f"Cannot open {self.directory}")
        else:
            for file in files:
                if not file.endswith('py'):
                    continue
                else:
                    try:
                        fp = open(file, 'r')
                    except FileNotFoundError:
                        raise FileNotFoundError("Cannot open file")
                    else:
                        total_lines = 0
                        total_char = 0
                        total_function = 0
                        total_class = 0
                        for line in fp:
                            total_lines += 1
                            total_char += len(line)
                            line = line.strip()
                            if line.startswith('def'):
                                total_function += 1
                            if line.startswith('class'):  # provide spacing after class_
                                total_class += 1
                        self.files_summary[self.directory] = {'line': total_lines, 'char': total_char,
                                                              'function': total_function, 'class': total_class}

    def pretty_print(self):
        """ use PrettyTable to format your table. """
        pretty_print1 = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Character'])
        for key, values in self.files_summary.items():
            pretty_print1.add_row([key, values['class'], values['function'], values['line'], values['char']])
        print(pretty_print1)


# file1 = FileAnalyzer(r'/home/akshay/PycharmProjects/tensorflow/Akshay1')  # os.changedir will help but risky
# print(file1)
