class Employee():
    a = 1

    @classmethod  # used to make a class method
    # instead of 'self' class methods takes 'cls' as argument
    def show(cls):
        print(f"The class attribute of a is {cls.a}.")

# NOTE: class method is bound to the class and not the object of the class.


e = Employee()
e.a = 45
e.show()

# self means --> object --> method. (object jis par method chal raha hai)
# cls means --> class --> object --> method (class ka vo object jis par method chal raha hai)
