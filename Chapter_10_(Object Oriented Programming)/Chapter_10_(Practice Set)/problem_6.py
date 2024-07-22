# Problem 6
# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

# ANSWER: Yes we can change the self-parameter and it does not make any effect but can reduce the readability.

class Programmer:
    company = "Microsoft"

    def __init__(slf, name, role, salary):
        slf.name = name
        slf.role = role
        slf.salary = salary


harry = Programmer("Harry", "Developer", 1200000)
print(harry.name, harry.company, harry.role, harry.salary)
