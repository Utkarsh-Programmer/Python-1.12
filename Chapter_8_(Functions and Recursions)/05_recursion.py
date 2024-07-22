# recursion is a function which call itself.
# recursion function calls itself until it reaches the base case.
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)


n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")
