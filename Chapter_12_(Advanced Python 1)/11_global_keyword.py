a = 89


def fun():
    global a  # changing to global variable
    a = 3  # local variable
    print(a)


fun()
print(a)  # 89 will be printed without global keyword


# `global` keyword is used to make a global variable that can be accesses inside and outside the functions.
# A local variable is that variable which have a limited scope.
