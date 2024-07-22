# Problem 5
# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [111, 2, 65, 6, 53, 1635, 65,]


def greater(a, b):
    if (a > b):
        return a
    else:
        return b


print(reduce(greater, l))
