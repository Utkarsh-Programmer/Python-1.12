# Problem 5
# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter a number to get its table: "))

with open(f"{n}_table.txt", "w") as f1:
    f1.write(f"{[n*i for i in range(1, 11)]}")
