# __init__() constructor first run as soon as an object is created.
# it takes 'self' argument and can take other arguments.

class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language):  # dunder method which is automatically called
        # these are instance attributes
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object.")

    def get_info(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


harry = Employee("Harry", 1200000, "Python")
print(harry.name, harry.language, harry.salary)

rohan = Employee("Rohan", 100000, "Java")
print(rohan.name, rohan.language, rohan.salary)


# NOTE: In Python methods starting with __(underscores) is known as 'dunder' methods.
# NOTE: __init__() dunder method automatically calls whenever an object is created.
