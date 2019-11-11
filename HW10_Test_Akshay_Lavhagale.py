""" Akshay Lavhagale
    Homework 10
    Build the framework for student, major and instructor project and summarize their data. """

import unittest
from HW10_Akshay_Lavhagale import Respository, Student, Instructor, Major


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.test_path = "/home/akshay/PycharmProjects/tensorflow"
        self.repo = Respository(self.test_path, False)

    def test_attributes(self):
        """ Test suit will check whether class Major hold all of details of a major, student and instructor or not """
        expected_major = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
                          ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]

        """ Test suit will check whether class Student hold all of the details of a student or not """
        expected_student = {'10103': ['10103', 'Baldwin, C', 'SFEN', {'SSW 564', 'CS 501', 'SSW 687', 'SSW 567'},
                                      {'SSW 555', 'SSW 540'}, None],
                            '10115': ['10115', 'Wyatt, X', 'SFEN', {'SSW 564', 'SSW 687', 'SSW 567', 'CS 545'},
                                      {'SSW 555', 'SSW 540'}, None],
                            '10172': ['10172', 'Forbes, I', 'SFEN', {'SSW 555', 'SSW 567'}, {'SSW 540', 'SSW 564'},
                                      {'CS 501', 'CS 545', 'CS 513'}],
                            '10175': ['10175', 'Erickson, D', 'SFEN', {'SSW 564', 'SSW 687', 'SSW 567'},
                                      {'SSW 555', 'SSW 540'}, {'CS 501', 'CS 545', 'CS 513'}],
                            '10183': ['10183', 'Chapman, O', 'SFEN', {'SSW 689'},
                                      {'SSW 555', 'SSW 540', 'SSW 564', 'SSW 567'}, {'CS 501', 'CS 545', 'CS 513'}],
                            '11399': ['11399', 'Cordova, I', 'SYEN', {'SSW 540'}, {'SYS 671', 'SYS 612', 'SYS 800'},
                                      None],
                            '11461': ['11461', 'Wright, U', 'SYEN', {'SYS 611', 'SYS 750', 'SYS 800'},
                                      {'SYS 671', 'SYS 612'}, {'SSW 540', 'SSW 810', 'SSW 565'}],
                            '11658': ['11658', 'Kelly, P', 'SYEN', set(), {'SYS 671', 'SYS 612', 'SYS 800'},
                                      {'SSW 540', 'SSW 810', 'SSW 565'}],
                            '11714': ['11714', 'Morton, A', 'SYEN', {'SYS 611', 'SYS 645'},
                                      {'SYS 671', 'SYS 612', 'SYS 800'}, {'SSW 540', 'SSW 810', 'SSW 565'}],
                            '11788': ['11788', 'Fuller, E', 'SYEN', {'SSW 540'},
                                      {'SYS 671', 'SYS 612', 'SYS 800'}, None]}

        """ Test suit will check whether class Instructor hold all of the details of a instructor or not """
        expected_instructor = {('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
                               ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
                               ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
                               ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
                               ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
                               ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
                               ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
                               ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
                               ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
                               ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
                               ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
                               ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)}

        majors = [major.pt_row() for major in self.repo._major.values()]
        students = {cwid: student.pt_row() for cwid, student in self.repo._students.items()}
        instructors = {tuple(row) for instructor in self.repo._instructors.values() for row in instructor.pt_row()}

        self.assertEqual(majors, expected_major)
        self.assertEqual(students, expected_student)
        self.assertEqual(instructors, expected_instructor)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
