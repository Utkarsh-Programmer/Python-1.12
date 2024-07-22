class Employee:
    language = "Python"  # class attribute
    salary = 1200000

    # Making method
    def get_info(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")


harry = Employee()
harry.language = "JavaScript"  # instance attribute

harry.get_info()
"""
harry.get_info() will be converted like this,
Employee.get_info(harry)
"""

# NOTE: self parameter is automatically passed when a function call from an object. self parameter refers to current instance of class self is the naming convention for the default attribute name in a method.
