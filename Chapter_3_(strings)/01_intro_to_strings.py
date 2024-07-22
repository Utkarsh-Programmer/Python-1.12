# NOTE: strings are immutable.

a = "Harry"  # double quoted string
b = 'Harry'  # single quoted string

c = '''Harry'''  # single quoted multiline string
d = """Harry"""  # double quoted multiline string


# String Slicing...
name = "Harry"
# normal indexing
print(name[0])
print(name[1])

# negative indexing
print(name[-1])
print(name[-2])

# positive slicing
print(name[1:4])

# negative slicing
print(name[-4:-1])

# NOTE: start argument is included whereas stop argument is excluded.

# slicing with step argument
word = "amazing"
print(word[1:6:2])
