# Problem 5
# write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a number: "))

total = 0
for i in range(1, n+1):
    total += i
print(total)
