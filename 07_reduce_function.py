from functools import reduce

l = [1, 2, 3, 4, 5]


def sum(a: int, b: int) -> int:
    return a+b


print(reduce(sum, l))  # 1+2=3, 3+3=6, 6+4=10, 10+5=15

# NOTE: `reduce` function is imported from the `functools` module. It repeatedly merges two iterable elements into ones, as defined by the function argument and return the final single value.
