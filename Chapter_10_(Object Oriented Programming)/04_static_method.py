class Employee:
    language = "Python"
    salary = 1200000

    # Making a static method, that doesn't require arguments.
    @staticmethod
    def greet():
        print("Good Morning!")


Employee.greet()
