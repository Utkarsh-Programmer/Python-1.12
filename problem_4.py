# Problem 4
# Write a program to filter a list of numbers which are divisible by 5.

def divisibles(n):
    if n % 5 == 0:
        return True
    else:
        return False


a = [1, 2, 5, 567, 434, 55, 8, 89, 34]

f = list(filter(divisibles, a))
print(f)
