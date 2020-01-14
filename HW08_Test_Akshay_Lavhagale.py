""" Akshay Lavhagale
    Homework 08
    Practice and learn Date Arithmetic Operations, field separated file reader and Scanning directories and files """

import unittest
from HW08_Akshay_Lavhagale import date_arithmetic, file_reading_gen, FileAnalyzer


class TestModuleGeneratorFile(unittest.TestCase):
    def test_date_arithmetic(self):
        """ Write a function date_arithmetic to use Python’s datetime module """
        expected = '3 days after 02/27/2000 is 03/01/2000', '3 days after 02/27/2017 is 03/02/2017', \
                   '01/01/2017 occurs 299 days before 10/27/2017'
        result = date_arithmetic()
        self.assertEqual(result, expected)

    def test_file_reading_gen(self):
        """ Generator function file_reading_gen to read field-separated text files and yield a tuple with all of
            the values from a single line in the file on each call to next() """
        self.path = "student_majors.txt"
        expect = [('123', 'Jin He', 'Computer Science'),
                  ('234', 'Nanda Koka', 'Software Engineering'),
                  ('345', 'Benji Cai', 'Software Engineering')]
        result = list(file_reading_gen(r"student_majors.txt", 3, sep='|', header=True))
        self.assertEqual(result, expect)

    def test_analyze_files(self):
        """ For each .py file, open each file and calculate a summary of the file """
        # directory = ''
        expect = {'0_defs_in_this_file.py': {'line': 3, 'char': 57, 'function': 0, 'class': 0}, 'file1.py': {'line': 25
                  , 'char': 270, 'function': 4, 'class': 2}}
        result = FileAnalyzer(r"/home/akshay/PycharmProjects/tensorflow/Akshay1").files_summary
        # fa = FileAnalyzer
        self.assertEqual(expect, result)  # self.assertEqual(fa.files_summary, expect)

        # how decorators work


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)  # these are the parameters and will use help(unittest.main)
