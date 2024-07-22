# Problem 2
# Write a class “Calculator” capable of finding square, cube and square root of a number.

import math


class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"Square of {self.number} is {self.number**2}")

    def cube(self):
        print(f"Cube of {self.number} is {self.number**3}")

    def square_root(self):
        print(f"Square Root of {self.number} is {math.sqrt(self.number)}")


calc = Calculator(2)

calc.square()
calc.cube()
calc.square_root()