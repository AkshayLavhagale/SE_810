""" Akshay Lavhagale
    SSW 810 - Homework_03-Fractions
    Implement a fraction calculator that asks the user for two fractions and an operator and then prints the result.
 """

import unittest


# Calculating greatest common denominator.
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    # self - memory allocation for particular class.
    def __init__(self, numerator, denominator):
        self.numerator = numerator  # self.numerator - Initializing attributes in new instance of class Fraction.
        self.denominator = denominator
        if denominator == 0:
            raise ZeroDivisionError("Denominator should not be zero")

    # Returns string to describe instance of class.
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    # Addition of Fractions
    def __add__(self, a):  # Methods are functions inside class.
        newnumerator = self.numerator * a.denominator + self.denominator * a.numerator
        newdenominator = self.denominator * a.denominator
        common = gcd(newnumerator, newdenominator)
        return Fraction(newnumerator // common, newdenominator // common)

    # Subtraction of Fractions
    def __sub__(self, a):
        newnumerator = self.numerator * a.denominator - self.denominator * a.numerator
        newdenominator = self.denominator * a.denominator
        common = gcd(newnumerator, newdenominator)
        return Fraction(newnumerator // common, newdenominator // common)

    # Multiplication of Fractions
    def __mul__(self, a):
        newnumerator = self.numerator * a.numerator
        newdenominator = self.denominator * a.denominator
        common = gcd(newnumerator, newdenominator)
        return Fraction(newnumerator // common, newdenominator // common)

    # Division of Fractions
    def __truediv__(self, a):
        newnumerator = self.numerator * a.denominator
        newdenominator = self.denominator * a.numerator
        common = gcd(newnumerator, newdenominator)
        return Fraction(newnumerator // common, newdenominator // common)

    # If two fractions are equal
    def __eq__(self, a):
        firstno = self.numerator * a.denominator
        secondno = self.denominator * a.numerator
        return firstno == secondno

    # If two fractions are not equal
    def __ne__(self, a):
        firstno = self.numerator * a.denominator
        secondno = self.denominator * a.numerator
        return firstno != secondno

    # If one fraction is less than other
    def __lt__(self, a):
        firstno = self.numerator * a.denominator
        secondno = self.denominator * a.numerator
        return firstno < secondno

    # If one fraction is less than or equal to other fraction
    def __le__(self, a):
        firstno = self.numerator * a.denominator
        secondno = self.denominator * a.numerator
        return firstno <= secondno

    # If greater than
    def __gt__(self, a):
        firstno = self.numerator * a.denominator
        secondno = self.denominator * a.numerator
        return firstno > secondno

    # If greater than or equal to
    def __ge__(self, a):
        firstno = self.numerator * a.denominator
        secondno = self.denominator * a.numerator
        return firstno >= secondno


def main():
    # test cases
    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    f128 = Fraction(12, 8)
    f32 = Fraction(3, 2)

    print(f"{f12} + {f12} = {f12.__add__(f12)} [1/1]")
    print(f"{f44} - {f12} = {f44.__sub__(f12)} [1/2]")
    print(f"{f12} + {f44} = {f12.__add__(f44)} [3/2]")
    print(f"{f128} == {f32} is {f128.__eq__(f32)} [True]")

    x = Fraction(int(input("Fraction 1 numerator= ")), int(input("Fraction 1 denominator= ")))
    y = Fraction(int(input("Fraction 2 numerator= ")), int(input("Fraction 2 denominator= ")))
    operator = input("+ for add, - for sub, * for mul, / for div, == for eq, != for ne, < for lt, \
     <= for ne, > for gt, >= for ge: ")
    if operator == "+":
        print(x, operator, y, (x+y))
    elif operator == "-":
        print(x, operator, y, (x-y))
    elif operator == "*":
        print(x, operator, y, (x*y))
    elif operator == "/":
        print(x, operator, y, (x/y))
    elif operator == "==":
        print(x, operator, y, (x == y))
    elif operator == "!=":
        print(x, operator, y, (x != y))
    elif operator == "<":
        print(x, operator, y, (x < y))
    elif operator == "<=":
        print(x, operator, y, (x <= y))
    elif operator == ">":
        print(x, operator, y, (x > y))
    elif operator == ">=":
        print(x, operator, y, (x >= y))
    else:
        print("you have given me the invalid operator")
    print(x, operator, y)


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


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

import unittest
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

class Fraction:
    def __init__(self, num, den):
        """ function init has parameter that class Fraction will use: Numerator, denominator """
        self.num = num
        self.den = den
        if den < 0:
            self.num = -1 * self.num
            self.den = -1 * self.den
        if den == 0:
            raise ZeroDivisionError("The denominator cant be zero")

    def __add__(self, other):
        """ Add the fractions """
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __sub__(self, other):
        """ Subtract the fractions """
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __mul__(self, other):
        """ multiply the fractions """
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        """ division of fractions """
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __eq__(self, other):
        """ provide return values of True or False if two fractions are equal """
        if self.num * other.den == self.den * other.num:
            return True
        else:
            return False

    def __ne__(self, other):
        """ provide return values of True or False if two fractions are not equivalent """
        if self.num * other.den != self.den * other.num:
            return True
        else:
            return False

    def __lt__(self, other):
        """ compare less than of two fractions return True/False """
        if self.num * other.den < self.den * other.num:
            return True
        else:
            return False

    def __le__(self, other):
        """ compare the two fractions for less than and equal and return True/False """
        if self.num * other.den <= self.den * other.den:
            return True
        else:
            return False

    def __gt__(self, other):
        """ compare the greater than for two fractions and return True/False """
        if self.num * other.den > self.den * other.num:
            return True
        else:
            return False

    def __ge__(self, other):
        """ compare the greater than and equal to for two fractions and return True/False """
        if self.num * other.den >= self.den * other.num:
            return True
        else:
            return False

    def __str__(self):
        """ string to display fractions """
        return str(self.num) + "/" + str(self.den)

def get_int(prompt):
    """ Function get_int makes sure that user inserts integer. if user does not enter integer then exception cathes """
    while True:
        value = input(prompt)
        try:
            i = int(value)
            return i
        except ValueError:
            print("please enter an integer")

def get_fraction():
    """ function get an input of num and den. if input of den is 0 then raises exception """
    while True:
        num = get_int("Enter numerator: ")
        den = get_int("Enter denominator: ")
        try:
            return Fraction(num, den)
        except ZeroDivisionError as e:
            print(e)

def get_operation():
    """ get the operators and try to use it in different condition of fractions """
    f1 = get_fraction()
    while True:
        operation = input("operation(+,-,*,/,==, !=, <, <=, >, >=): ")
        if operation not in ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=']:
            print("Wrong Operation")
        else:
            break
    f2 = get_fraction()
    if operation == '+':
        return f1 + f2
    elif operation == '-':
        return f1 - f2
    elif operation == "*":
        return f1 * f2
    elif operation == "/":
        return f1 / f2
    elif operation == "==":
        return f1 == f2
    elif operation == "!=":
        return f1 != f2
    elif operation == "<":
        return f1 < f2
    elif operation == "<=":
        return f1 <= f2
    elif operation == ">":
        return f1 > f2
    else:
        return f1 >= f2

class TestFraction(unittest.TestCase):
    def test_init(self):
        """verify that numerator and denominator are set properly """
        f = Fraction(3, 4)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.den, 4)
        with self.assertRaises(ZeroDivisionError):
            f = Fraction(1, 0)

    def test_str(self):
        """ verify that __str__ work properly """
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3/4')

    def test_plus(self):
        """ test fraction addition """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(-1, 3)
        f4 = Fraction(0, 4)
        self.assertTrue((f1 + f1) == Fraction(6, 4))
        self.assertTrue((f1 + f2 + f3) == Fraction(11, 12))
        self.assertTrue((f3 + f4) == Fraction(-1, 3))