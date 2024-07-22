# Problem 1
# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class two_d_vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class three_d_vector(two_d_vector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


a = two_d_vector(1, 2)
b = three_d_vector(1, 2, 2)
b.show()
