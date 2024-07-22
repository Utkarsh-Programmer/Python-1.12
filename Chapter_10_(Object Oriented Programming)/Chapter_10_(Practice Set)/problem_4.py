# Problem 4
# Add a static method in problem 2, to greet the user with hello.

import math


class Calculator:
    @staticmethod
    def greet():
        print("Hello there!")

    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"Square of {self.number} is {self.number**2}")

    def cube(self):
        print(f"Cube of {self.number} is {self.number**3}")

    def square_root(self):
        print(f"Square Root of {self.number} is {math.sqrt(self.number)}")


calc = Calculator(2)

calc.greet()
calc.square()
calc.cube()
calc.square_root()
