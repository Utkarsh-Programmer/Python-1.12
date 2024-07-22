# Problem 1
# write a program using functions to find greatest of three numbers.

def find_greatest(a, b, c):
    if a > b and a > c:
        print(f"{a} is greater.")
    elif b > a and b > c:
        print(f"{b} is greater.")
    else:
        print(f"{c} is greater.")


find_greatest(5, 3, 7)
