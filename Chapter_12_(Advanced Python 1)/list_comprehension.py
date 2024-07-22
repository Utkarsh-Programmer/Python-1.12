# NOTE: list comprehension is the most elegant way to create a list from the existing list.

my_list = [1, 2, 3, 4, 5]

squared_list = [i*i for i in my_list]
print(squared_list)


# SYNTAX = variable = [expression for item in iterable if condition]
# if condition is only used if required.
