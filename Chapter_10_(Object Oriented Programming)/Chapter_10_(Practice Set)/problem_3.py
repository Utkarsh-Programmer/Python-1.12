# Problem 3
# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

# ANSWER: No

class Demo:
    a = "Rohan"  # class attribute


obj = Demo()
obj.a = 0  # instance attribute

print(obj.a)
print(Demo.a)
