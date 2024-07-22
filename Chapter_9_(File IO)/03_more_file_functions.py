f = open("file.txt")
""" lines = f.readlines()  # return file data as a list with a '\n'.
print(lines)
print(type(lines)) """


line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()  # it doesn't exist
print(line5, type(line5))  # so, it return an empty string, which cannot be seen
print(line5 == "")  # proof, that the above line return an empty string

f.close()

# NOTE: there are many more methods and file modes in python. Check ChatGPT.
