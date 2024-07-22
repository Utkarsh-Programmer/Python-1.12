# Exception handling prevents the program from crashing.
try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Integer expected!")
except Exception as e:
    # prints the default message, invalid literal for int with base 10.
    print(e)

print("Thankyou!")
