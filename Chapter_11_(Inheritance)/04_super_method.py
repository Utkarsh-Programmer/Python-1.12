class Employee:
    def __init__(self):
        print("Constructor of Employee.")
    a = 1


class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer.")
    b = 2


# NOTE: super method is used access the methods of a super class in the derived class.
class Manager(Programmer):
    def __init__(self):
        # access methods of the 'Employee' class which is a super class of 'Manager' class.
        super().__init__()
        print("Constructor of Manager.")
    c = 3


# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a)

o = Manager()
print(o.a)
