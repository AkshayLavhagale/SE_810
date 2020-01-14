""" Akshay Lavhagale
    SSW 810 - Homework 05
    Testing of string methods and automated testing """

import unittest
from HW05_Akshay_Lavhagale import reverse, rev_enumerate, find_second, get_lines


class TestReverse(unittest.TestCase):
    def test_reverse(self):
        """ Testing the function that takes a string as an argument and returns a new string """
        self.assertTrue((reverse('hello world')) == 'dlrow olleh')
        self.assertFalse((reverse('hello world')) == 'olleh dlrow')
        self.assertEqual((reverse('AKSHAY')), 'YAHSKA')
        self.assertNotEqual((reverse('akshay')), 'yhska')
        self.assertEqual((reverse('')), '')

    def test_rev_enumerate(self):
        """ Testing a generator that return elements in the sequence from last to first with corresponding offset """
        expected_result = [(6, 's'), (5, 'n'), (4, 'e'), (3, 'v'), (2, 'e'), (1, 't'), (0, 's')]
        result = list(rev_enumerate("stevens"))
        self.assertEqual(result, expected_result)

        expected_result2 = [(4, 'a'), (3, 'h'), (2, 's'), (1, 'k'), (0, 'a')]
        result2 = list(rev_enumerate("akshay"))
        self.assertNotEqual(result2, expected_result2)

        expected_result1 = [(4, 'i'), (3, 's'), (2, 's'), (1, 'e'), (0, 'm')]
        result1 = list(rev_enumerate("messi"))
        self.assertTrue(result1 == expected_result1)

        expected_result3 = [(4, 'a'), (3, 'h'), (2, 's'), (1, 'k'), (0, 'a')]
        result3 = list(rev_enumerate("ahska"))
        self.assertFalse(result3 == expected_result3)

        expected_result4 = []
        result4 = list(rev_enumerate([]))
        self.assertEqual(result4, expected_result4)

    def test_find_second(self):
        """ Testing whether offset returns second occurrence of s1 in s2 """
        self.assertTrue((find_second('iss', 'Mississippi')) == 4)
        self.assertFalse((find_second('iss', 'Mississippi')) == 1)
        self.assertEqual((find_second('ana', 'banana')), 3)
        self.assertNotEqual((find_second('ana', 'banana')), 1)

    def test_get_lines(self):
        """ Testing the combining of lines and removal of comments """
        expected_result = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>',
                           '<line5>', '<line6>']
        result = list(get_lines("test1.txt"))
        self.assertTrue(result == expected_result)

        expected_result1 = ['<line0>', '<line1>', '<line2>', '<line3.1>', '<line3.2>', '<line3.3>',
                            '<line4.1 line4.2>', '<line5>', '<line6>']
        result1 = list(get_lines("test1.txt"))
        self.assertFalse(result1 == expected_result1)

        expected_result2 = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>',
                            '<line5>', '<line6>']
        result2 = list(get_lines("test1.txt"))
        self.assertEqual(result2, expected_result2)

        expected_result3 = ['<line0>', '<line1>', '<line2>', '<line3.1>', '<line3.2>', '<line3.3>',
                            '<line4.1 line4.2>', '<line5>', '<line6>']
        result3 = list(get_lines("test1.txt"))
        self.assertNotEqual(result3, expected_result3)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
