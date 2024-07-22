l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even(n):
    if n % 2 == 0:
        return True
    else:
        return False


only_even = filter(even, l)
print(list(only_even))


# NOTE: `filter` function allows us to process an iterable and extract items that satisfy the given condition.
