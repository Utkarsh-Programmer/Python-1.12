# Making a class
class Employee:
    language = "Python"
    salary = 1200000


"""
Employee class has three attributes --> name, language, salary
Attributes that directly belongs to a class are known as 'class attributes'.
"""

# NOTE: class name should be in PascalCase.


# Making an object
harry = Employee()

# Making 'instance attribute'
harry.name = "Harry"

# Accessing attributes
print(harry.name, harry.language, harry.salary)
