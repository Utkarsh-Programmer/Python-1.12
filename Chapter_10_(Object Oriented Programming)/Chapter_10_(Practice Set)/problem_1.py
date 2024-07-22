# Problem 1
# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary


harry = Programmer("Harry", "Developer", 1200000)
print(harry.name, harry.company, harry.role, harry.salary)
