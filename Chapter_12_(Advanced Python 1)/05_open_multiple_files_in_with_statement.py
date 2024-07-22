with (
    open("file1.txt", "w") as f1,
    open("file2.txt", "w") as f2
):
    f1.write("Hello World!")
    f2.write("Hello World!")
