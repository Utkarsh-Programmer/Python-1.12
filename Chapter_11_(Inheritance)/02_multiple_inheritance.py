# This is the parent/base class for the 'Programmer' class
class Employee:
    company = "ITC"
    name = "Keven"

    def show(self):
        print(f"The name is {self.name} and the your company is {
              self.company}.")


class Coder:
    language = "Python"

    def print_languages(self):
        print(f"Out of the languages here is your language {
            self.language}.")


class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def show_language(self):
        print(f"The company is {self.company} which works with {
              self.language} language.")


a = Employee()
b = Programmer()

b.show()
b.show_language()
b.print_languages()
