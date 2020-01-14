""" Akshay Lavhagale
    SSW 810 - Homework 06
    From part 1 to 5 try to implement list comprehensions and in part 6 sorting list in ascending order
"""

import unittest
from HW06_Akshay_Lavhagale import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, insertion_sort


class TestList(unittest.TestCase):
    def test_list_copy(self):
        """ take a list as a parameter and returns a copy of the list """
        self.assertEqual((list_copy([1, 2, 3])), [1, 2, 3])
        self.assertEqual((list_copy([1, 2, 3, ['stevens']])), [1, 2, 3, ['stevens']])
        self.assertNotEqual((list_copy([1, 2, 3])), [1, 2, ])
        self.assertEqual((list_copy([])), [])

    def test_list_intersect(self):
        """ takes two lists as  parameters and returns a new list with the values that are included in both list """
        self.assertEqual((list_intersect([1, 2, 3, ['stevens']], [1, 2, 4, ['stevens']])), [1, 2, ['stevens']])
        self.assertNotEqual((list_intersect([1, 2, 3], [1, 2, 4])), [3, 4])
        self.assertEqual((list_intersect([], [])), [])

    def test_list_difference(self):
        """ takes two lists as  parameters and returns a new list with the values that are  in l1, but not in l2 """
        self.assertEqual((list_difference([1, 2, 3], [1, 2, 4])), [3])
        self.assertEqual((list_difference([1, 2, 3], [1, 2, 3])), [])
        self.assertEqual((list_difference([1, 2, 3, ['stevens']], [1, 2, 4])), [3, ['stevens']])
        self.assertNotEqual((list_difference([1, 2, 3], [1, 2, 44])), [44])
        self.assertEqual((list_difference([1, 2, 3, 4], [5, 6, 7, 8])), [1, 2, 3, 4])
        self.assertEqual((list_difference([], [])), [])

    def test_remove_vowels(self):
        """ returns a copy of the string with no vowels """
        self.assertEqual((remove_vowels('hello world')), 'hll wrld')
        self.assertEqual((remove_vowels('hEllo world')), 'hll wrld')
        self.assertEqual((remove_vowels('hll wrld')), 'hll wrld')
        self.assertNotEqual((remove_vowels('hello world')), 'hllo world')
        self.assertEqual((remove_vowels('')), '')

    def test_check_pwd(self):
        """ take a string as a parameter, test that it includes all three parameters and returns a boolean value """
        self.assertEqual((check_pwd('Akshay1')), True)
        self.assertNotEqual((check_pwd('Akshay')), True)
        self.assertEqual((check_pwd('Akshay')), False)
        self.assertNotEqual((check_pwd('Akshay1')), False)
        self.assertEqual((check_pwd('')), False)

    def test_insertion_sort(self):
        """ returns a copy of the argument sorted using a list and the insertion sort algorithm """
        self.assertEqual((insertion_sort([1, 5, 3, 3])), [1, 3, 3, 5])
        self.assertNotEqual((insertion_sort([1, 5, 3, 3])), [1, 5, 3, 3])
        self.assertEqual((insertion_sort([])), [])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
