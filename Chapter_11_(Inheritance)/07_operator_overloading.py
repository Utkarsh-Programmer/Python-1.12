# NOTE: operators in python can be overloaded using dunder methods.

class Number:
    def __init__(self, n):
        self.n = n

    # Operator Overloading
    # addition
    def __add__(self, num):
        return self.n + num.n

    # subtraction
    def __sub__(self, num):
        return self.n - num.n

    # multiplication
    def __mul__(self, num):
        return self.n * num.n

    # division
    def __truediv__(self, num):
        return self.n / num.n

    # floor division
    def __floordiv__(self, num):
        return self.n // num.n


n = Number(1)
m = Number(2)

print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n//m)

# __str__() is used set what get displays upon calling print function or typecasting to string.
# __len__() is used to set what get displays upon calling the len function.
