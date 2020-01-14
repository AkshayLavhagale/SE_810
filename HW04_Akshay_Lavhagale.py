""" Akshay Lavhagale
    SSW 810 - Homework 04
    Practice iterating over lists, ranges, and strings using for and while loops as well as using a generator of
    random integers.
"""


# Part 1: count_vowels(self)
def count_vowels(string):
    """ Here we are taking the string as an argument and returns the number of vowels in the string """
    count = 0
    string = string.lower()
    for char in string:
        if char in 'aeiou':
            count += 1
    return count


# Part 2: last_occurrence(target, sequence)
def last_occurence(target, sequence):
    """ Here we are checking whether or not target is present in our string or not
        Return the index (offset from 0) of the last occurrence of the target item or None if the target is not found.
        """
    for offset, c in enumerate(reversed(sequence)):
        if c == target:
            return offset
    return None


# Calculating greatest common denominator.
def gcf(a, b):
    while a % b != 0:
        prev_a = a
        prev_b = b
        a = prev_b
        b = prev_a % prev_b
    return b


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
        common = gcf(newnumerator, newdenominator)
        return Fraction(newnumerator // common, newdenominator // common)

    # Subtraction of Fractions
    def __sub__(self, a):
        newnumerator = self.numerator * a.denominator - self.denominator * a.numerator
        newdenominator = self.denominator * a.denominator
        common = gcf(newnumerator, newdenominator)
        return Fraction(newnumerator // common, newdenominator // common)

    # Multiplication of Fractions
    def __mul__(self, a):
        newnumerator = self.numerator * a.numerator
        newdenominator = self.denominator * a.denominator
        common = gcf(newnumerator, newdenominator)
        return Fraction(newnumerator // common, newdenominator // common)

    # Division of Fractions
    def __truediv__(self, a):
        newnumerator = self.numerator * a.denominator
        newdenominator = self.denominator * a.numerator
        common = gcf(newnumerator, newdenominator)
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

    # Part 3: Fraction.simplify()
    # Adding new method Fraction.simplify()
    def simplify(self):
        """ Here we are trying to simplify fraction, e.g., 2/4 can be simplified to 1/2 """
        gcf = 2
        while gcf <= self.numerator and gcf <= self.denominator:
            if self.numerator % gcf == 0 and self.denominator % gcf == 0:
                self.numerator = self.numerator // gcf
                self.denominator = self.denominator // gcf
            else:
                gcf = gcf + 1
        return self


# Part 4: my_enumerate(seq)
def my_enumerate(seq):
    """ Here we are writing function for generator that returns values on each call """
    count = 0
    for elem in seq:
        yield count, elem
        count += 1
