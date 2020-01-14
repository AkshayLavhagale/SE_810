""" Akshay Lavhagale
    SSW 810 - Homework 04
    Practice iterating over lists, ranges, and strings using for and while loops as well as using a generator of
    random integers.
 """

import unittest
from HW04_Akshay_Lavhagale import Fraction, count_vowels, last_occurence, my_enumerate


class TestFraction(unittest.TestCase):
    def test_init(self):
        """ this is to check whether numerator and denominator were set correctly or not """
        f = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)
        if self.assertEqual == 0:
            raise ValueError("Denominator should not be zero")

    def test_str(self):
        """ this is to check whether __self__ works correctly or not """
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3/4')

    def test_equal(self):
        """ this is to check test fraction equality """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        self.assertTrue(f1 == f1)
        self.assertTrue(f2 == f2)
        self.assertTrue(f3 == f3)
        self.assertTrue(f2 == f3)
        self.assertFalse(f1 == (Fraction(3, 5)))

    def test_add(self):
        """ this is to check test fraction addition """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 + f1) == Fraction(3, 2))
        self.assertTrue((f1 + f2) == Fraction(5, 4))
        self.assertTrue((f1 + f3) == Fraction(13, 12))

    def test_sub(self):
        """ this is to check test fraction subtraction """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 - f1) == Fraction(0, 1))
        self.assertTrue((f1 - f2) == Fraction(1, 4))
        self.assertTrue((f1 - f3) == Fraction(5, 12))

    def test_mul(self):
        """ this is to check test fraction multiplication """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 * f1) == Fraction(9, 16))
        self.assertTrue((f1 * f2) == Fraction(3, 8))
        self.assertTrue((f1 * f3) == Fraction(1, 4))

    def test_truediv(self):
        """ this is to check test fraction division """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 / f1) == Fraction(1, 1))
        self.assertTrue((f1 / f2) == Fraction(3, 2))
        self.assertTrue((f1 / f3) == Fraction(9, 4))

    def test_ne(self):
        """ this is to check test fraction are not equal """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(9, 10)
        self.assertTrue(f1 != f2)
        self.assertTrue(f1 != f3)
        self.assertTrue(f2 != f3)
        self.assertFalse(f1 != (Fraction(3, 4)))

    def test_lt(self):
        """ this is to check one test fraction is less than other or not """
        f1 = Fraction(1, 2)
        f2 = Fraction(10, 8)
        f3 = Fraction(16, 8)
        self.assertTrue(f1 < f2)
        self.assertTrue(f2 < f3)
        self.assertTrue(f1 < f3)
        self.assertFalse(f1 < (Fraction(1, 2)))

    def test_le(self):
        """ this is to check one test fraction is less than or equal to other or not """
        f1 = Fraction(1, 2)
        f2 = Fraction(10, 8)
        f3 = Fraction(16, 8)
        self.assertTrue(f1 <= f2)
        self.assertTrue(f2 <= f3)
        self.assertTrue(f1 <= f3)
        self.assertFalse(f1 <= (Fraction(1, 4)))

    def test_gt(self):
        """ this is to check one test fraction is greater than other or not """
        f1 = Fraction(9, 10)
        f2 = Fraction(7, 8)
        f3 = Fraction(4, 6)
        self.assertTrue(f1 > f2)
        self.assertTrue(f2 > f3)
        self.assertTrue(f1 > f3)
        self.assertFalse(f1 > (Fraction(9, 10)))

    def test_ge(self):
        """ this is to check one test fraction is greater than or equal to other or not """
        f1 = Fraction(9, 10)
        f2 = Fraction(7, 8)
        f3 = Fraction(11, 12)
        self.assertTrue(f1 >= f2)
        self.assertTrue(f3 >= f1)
        self.assertTrue(f3 >= f1)
        self.assertFalse(f1 >= (Fraction(10, 10)))


class TestIteration(unittest.TestCase):
    def test_count_vowels(self):
        """ Checking the string as an argument and returns the number of vowels in the string """
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)
        self.assertNotEqual(count_vowels('hll wrld'), 1)

    def test_last_occurence(self):
        """ Here we are checking whether or not target is present in our string or not """
        self.assertEqual(last_occurence(target='p', sequence='apple'), 2)
        self.assertEqual(last_occurence(target=33, sequence=[42, 33, 21]), 1)
        self.assertEqual(last_occurence(target=21, sequence=[42, 33, 21]), 0)
        self.assertNotEqual(last_occurence(target=10, sequence=[42, 33, 21]), 1)

    def test_simplify(self):
        """ Checking whether or not our fraction got simplified or not """
        self.assertEqual(str(Fraction(9, 27).simplify()), str(Fraction(1, 3)))
        self.assertEqual(str(Fraction(6, 15).simplify()), str(Fraction(2, 5)))
        self.assertTrue(str(Fraction(-9, -27).simplify()), str(Fraction(-1, -3)))
        self.assertNotEqual(str(Fraction(11, 22).simplify()), str(Fraction(1, 3)))

    def test_my_enumerate(self):
        """ Checking whether our generator returning same values or not """
        self.assertTrue(list(my_enumerate(["akshay"])) == list(enumerate(["akshay"])))
        self.assertFalse(list(my_enumerate(["akshay"])) == list(enumerate(["akhay"])))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
