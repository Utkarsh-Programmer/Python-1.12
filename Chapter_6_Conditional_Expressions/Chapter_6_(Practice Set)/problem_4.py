# Problem 4
# write a program to find whether a given username contains less than 10 characters or not .

username = input("Enter your username: ")

if len(username) > 10:
    print("Ok!")
    print("Your username contains", len(username), "characters.")
else:
    print("Your username contains only", len(username), "characters.")
