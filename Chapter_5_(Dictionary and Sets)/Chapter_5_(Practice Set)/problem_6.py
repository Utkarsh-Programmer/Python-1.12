# Problem 6
# create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter your name: ")
lang = input("Enter your favorite language: ")
d.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your favorite language: ")
d.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your favorite language: ")
d.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your favorite language: ")
d.update({name: lang})

print(d)
