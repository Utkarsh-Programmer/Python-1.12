st = "Appending some text."

f = open("myfile.txt", "a")  # open file in the append mode.
f.write(st)
f.close()
