""" Akshay Lavhagale
    SSW 810 - Homework_02-Fractions
    Implement a fraction calculator that asks the user for two fractions and an operator and then prints the result.
 """


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


# test cases
f12 = Fraction(1, 2)
f44 = Fraction(4, 4)
f128 = Fraction(12, 8)
f32 = Fraction(3, 2)

print((f12 + f12), "Expected Result = 1/1")
print((f44 - f12), "Expected Result = 1/2")
print((f12 + f44), "Expected Result = 3/2")
print((f128 == f32), "Expected Result = True")

x = Fraction(int(input("Fraction 1 numerator= ")), int(input("Fraction 1 denominator= ")))
y = Fraction(int(input("Fraction 2 numerator= ")), int(input("Fraction 2 denominator= ")))
operator = input("+ for add, - for sub, * for mul, / for div, == for eq: ")
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
else:
    print("you have given me the invalid operator")
print(x, operator, y)
