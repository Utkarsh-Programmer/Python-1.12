age = int(input("Enter your age: "))

if age % 2 == 0:
    print("age is even")

if age > 18:
    print("You are above the age of concent.")
    print("Good Bye!")
elif age < 0:
    print("You are entering an invalid age.")
else:
    print("You are below the age of concent.")

print("End of Program.")
