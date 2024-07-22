l = [1, 2, 3, 4, 5]


def square(x): return x**2  # function to be used in the map function.


sq_list = map(square, l)
print(list(sq_list))


# NOTE: `map` function allows us to apply a given function to each item in an iterable.
