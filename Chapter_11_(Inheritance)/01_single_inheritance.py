# This is the parent/base class for the 'Programmer' class
class Employee:
    company = "ITC"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}.")


# Class with inheritance
# This inherited class access all methods and attributes of the  parent/base class.
# It is also known as derived/child class.
class Programmer(Employee):
    company = "ITC Infotech"

    def show_language(self):
        print(f"The name is {self.name} and he is good with {
              self.language} language.")


a = Employee()
b = Programmer()

print(a.company, b.company)

# NOTE: there are three types of inheritance,
# single inheritance --> when derived class inherits only one base class.
# multiple inheritance --> when derived class inherits multiple base classes.
# multilevel inheritance --> when child class becomes a base class for other derived class.
