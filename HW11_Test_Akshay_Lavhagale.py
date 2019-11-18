""" Akshay Lavhagale
    Homework 11
    Build the framework for student, major and instructor project and summarize their data. """

import unittest
from HW11_Akshay_Lavhagale import Repository


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.test_path = "/home/akshay/PycharmProjects/tensorflow"
        self.repo = Repository(self.test_path, False)

    def test_attributes(self):
        """ Test suit will check whether class Major hold all of details of a major, student and instructor or not """
        expected_major = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']],
                          ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]

        """ Test suit will check whether class Student hold all of the details of a student or not """
        expected_student = ({'10103': ['10103', 'Jobs, S', 'SFEN', {'SSW 810', 'CS 501'}, {'SSW 540', 'SSW 555'}, None],
                            '10115': ['10115', 'Bezos, J', 'SFEN', {'SSW 810'}, {'SSW 540', 'SSW 555'}, {'CS 501', 'CS 546'}],
                            '10183': ['10183', 'Musk, E', 'SFEN', {'SSW 555', 'SSW 810'}, {'SSW 540'}, {'CS 501', 'CS 546'}],
                            '11714': ['11714', 'Gates, B', 'CS', {'CS 570', 'SSW 810', 'CS 546'}, set(), None],
                            '11717': ['11717', 'Kernighan, B', 'CS', set(), {'CS 570', 'CS 546'}, {'SSW 810', 'SSW 565'}]})

        """ Test suit will check whether class Instructor hold all of the details of a instructor or not """
        expected_instructor = {('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
                               ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4),
                               ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
                               ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
                               ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
                               ('98762', 'Hawking, S', 'CS', 'CS 570', 1)}

        """ Test suit will check whether class Instructor hold all of the details of a instructor or not """
        expected_instructor_1 = {('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
                                 ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4),
                                 ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
                                 ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
                                 ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
                                 ('98762', 'Hawking, S', 'CS', 'CS 570', 1)}

        majors = [major.pt_row() for major in self.repo._major.values()]
        students = {cwid: student.pt_row() for cwid, student in self.repo._students.items()}
        instructors = {tuple(row) for instructor in self.repo._instructors.values() for row in instructor.pt_row()}

        dbpath = "/home/akshay/PycharmProjects/tensorflow/810_startup.db"
        self.repo.instructor_table_db(dbpath)
        instructors_1 = {tuple(row) for instructor in self.repo._instructors.values() for row in instructor.pt_row()}

        self.assertEqual(majors, expected_major)
        self.assertEqual(students, expected_student)
        self.assertEqual(instructors, expected_instructor)
        self.assertEqual(instructors_1, expected_instructor_1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
