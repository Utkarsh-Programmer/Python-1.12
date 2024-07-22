# tuples are a collection of data created using round brackets, but tuples are immutable.
a = (1, 2, 5, 6)
print(a)
print(type(a))  # <class 'tuple'>

# empty tuple...
emp_tup = ()
print(emp_tup)
print(type(emp_tup))

# single element tuple...
one_tup = (1,)
print(one_tup)
print(type(one_tup))

# Tuple Methods...
# `count` method...
# return the number of times a specified element appears in the tuple.
b = (1, 1, 3, 343, 45, 5, 67, 67, False, None)
print(b.count(67))

# `index` method...
# return the index of first occurrence of a specified value in the tuple.
# NOTE: if the value is not found then raise a `ValueError`.
print(b.index(False))


# Unpacking Tuples...
my_tup = ("one", "two", "three")
a, b, c = my_tup
print(a)
print(b)
print(c)
