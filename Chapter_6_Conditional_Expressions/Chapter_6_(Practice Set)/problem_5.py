# Problem 5
# write a program which finds out whether a given name is present in a list or not.

names = ["Harry", "Mahira", "Shubham", "Divya"]
username = input("Enter your username: ")

if username in names:
    print(username, "is present the list of name.")
else:
    print("Your name is not present.")
