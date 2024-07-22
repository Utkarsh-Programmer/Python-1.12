class Employee:
    language = "Python"  # class attribute
    salary = 1200000


harry = Employee()
harry.language = "JavaScript"  # instance attribute

# Here, instance attribute will be printed instead of class attribute as they have higher preference.
print(harry.language, harry.salary)
