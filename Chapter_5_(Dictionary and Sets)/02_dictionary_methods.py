marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}

# `items` method...
# return all key-value pairs in the form of tuples inside a list.
print(marks.items())

# `keys` method...
# return all keys of the dictionary.
print(marks.keys())

# `values` method...
# return all values of the dictionary.
print(marks.values())

# `update` method...
# update the existing dictionary.
marks.update({"Harry": 99, "Sonam": 100})
print(marks["Harry"])  # value of `Harry` is changed to 99
print(marks["Sonam"])  # new item with key `Sonam` and value `100` is added

# `get` method...
# return the value of the specified keys and return `None` if the key is not present.
print(marks.get("Shivika"))  # None
print(marks.get("Harry"))

# `pop` method...
# returns the specified kay and returns the corresponding value. If key not found, raise `KeyError`.
popped_item = marks.pop("Sonam")
print(marks)
print("Value of popped item:", popped_item)

# `popitem` method...
# removes the last key-value pair from the dictionary and return it as a tuple. If key is not present then raise `KeyError`.
last_pop = marks.popitem()
print(marks)
print(last_pop)

# NOTE: there are many more dictionary methods. Check on ChatGPT.
