a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

# Here, if the second number is 0, then we raise a 'ZeroDivisionError' intentionally, with an error message.
if b == 0:
    raise ZeroDivisionError("Our program is not meant to divide numbers by 0.")
else:
    print(f"{a} / {b} = {a/b}")
