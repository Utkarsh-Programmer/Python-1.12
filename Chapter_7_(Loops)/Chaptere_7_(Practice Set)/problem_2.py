# Problem 2
# write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if name.lower().startswith("s"):
        print(name)

# NOTE: `startswith` method checks if a string starts with the prefix.
