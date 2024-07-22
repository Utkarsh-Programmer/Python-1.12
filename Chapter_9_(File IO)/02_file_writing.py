text = "Hey Harry you are awesome."

f = open("myfile.txt", "w")  # writing to the file
f.write(text)
f.close()

# NOTE: if a file does't exist and we try to open it in writing mode. Then it will be created after running the program.
