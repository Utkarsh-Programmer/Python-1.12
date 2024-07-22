# Problem 6
# write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(factorial)
