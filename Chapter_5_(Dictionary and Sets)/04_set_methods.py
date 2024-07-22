# NOTE:
# sets are unordered.
# sets are un-indexed.
# there is no way to change items in sets.
# sets cannot contain duplicate values.

s = {1, 5, 32, 54, 5, 5, 5, "Harry"}
print(s, type(s))

# Operations on sets...
# `len` function...
print(len(s))

# `add` method...
# adds single element in the existing set.
s.add(566)
print(s, type(s))


# `remove` method...
# remove a single element from the existing set.
s.remove(54)
print(s)

# `pop` method...
# removes an arbitrary(randomly chosen element from the set, as sets are unordered) element from the set and return it.
p = s.pop()
print(s)
print("Popped Element:", p)

# `clear` method...
# empties the set.
s.clear()
print(s)

# `union` method...
# used to combine elements from multiple sets into a new set.
s1 = {1, 45, 6}
s2 = {7, 8, 1, 78}
print(s1.union(s2))

# `intersection` method...
# used to find common elements between sets.
print(s1.intersection(s2))

# NOTE: there are many more methods in sets. Check ChatGPT.
