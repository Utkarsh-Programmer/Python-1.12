# Problem 1
# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

try:
    with open("1.txt") as f1:
        print(f1.read())
except FileNotFoundError:
    print("1.txt not found.")

try:
    with open("2.txt") as f2:
        print(f2.read())
except FileNotFoundError as e:
    print("2.txt not found.")

try:
    with open("3.txt") as f3:
        print(f3.read())
except FileNotFoundError as e:
    print("3.txt not found.")
