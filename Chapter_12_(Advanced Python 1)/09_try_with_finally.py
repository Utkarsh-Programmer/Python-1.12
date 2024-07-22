# 'finally' block executes anyway even if the function returns.
def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

    except ValueError:
        print("Integer expected!")
        return

    finally:
        print("I am inside finally.")

    # print("I am inside finally.") # this line doesn't work if the function returns.


main()
