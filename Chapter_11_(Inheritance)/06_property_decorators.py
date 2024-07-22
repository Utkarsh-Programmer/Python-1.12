class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}.")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        # 'split' method splits the the string where ever the spaces are present and return as a list
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45
e.show()

e.name = "Harry Khan"
print(e.name)