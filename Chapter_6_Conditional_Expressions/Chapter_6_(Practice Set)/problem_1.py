# Problem 1
# write a program to find the greatest of four numbers entered by the user.

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    print(n1, "is greater.")
elif n2 > n1 and n2 > n3 and n2 > n4:
    print(n2, "is greater.")
elif n3 > n1 and n3 > n2 and n3 > n4:
    print(n3, "is greater.")
elif n4 > n1 and n4 > n2 and n4 > n3:
    print(n4, "is greater.")
