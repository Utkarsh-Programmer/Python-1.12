# Problem 7
# if the names of 2 friends are same; what will happen to the program in problem 6?

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

# ANSWER: previous value will be updated with the new value.
