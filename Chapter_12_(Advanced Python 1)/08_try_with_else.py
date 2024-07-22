# 'else' block only executes when the 'try' block is executed successfully.
try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Integer expected!")
else:
    print("I am inside else")
