# Problem 9
# write a program to print the following star pattern. for n = 3
"""
* * * 
*   *     
* * * 
"""

n = int(input("Enter a number: "))

for i in range(1, n+1):
    # print stars `n` times in the first and last line
    if i == 1 or i == n:
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")
