# Problem 4
# write a recursive function to calculate the sum of first n natural numbers.

def calc_sum(n):
    if n == 1:
        return 1
    else:
        return calc_sum(n-1) + n


print(calc_sum(5))
