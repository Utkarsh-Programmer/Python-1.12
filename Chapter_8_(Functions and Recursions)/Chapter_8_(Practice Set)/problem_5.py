# Problem 5
# write a python function to print first n lines of the following pattern: for n = 3
"""
*** 
** 
*
"""


def draw(n):
    if n == 0:
        return
    print("*"*n)
    draw(n-1)


draw(3)
