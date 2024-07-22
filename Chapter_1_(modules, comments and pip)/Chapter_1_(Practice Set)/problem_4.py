# Problem 4
# print the contents of a directory using the `os` module. Search online for the function which does that.

# code generated from chatgpt...
import os

# Replace with the actual directory path
directory_path = "/Code-Playground"

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)
