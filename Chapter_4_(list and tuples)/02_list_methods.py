# list methods doesn't return a new list, instead they change the original list.
friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]


# `append` method...
# add element to the end of the list.
friends.append("Harry")
print(friends)

# `sort` method...
# sorts the list in ascending or descending order.
num_list = [1, 34, 62, 2, 6, 11]
num_list.sort()
# num_list.sort(reverse=True) # it sort the list in descending order.
print(num_list)

word_list = ["apple", "mango", "papaya", "kiwi", "pineapple", "banana"]
word_list.sort()
print(word_list)

# `reverse` method...
# reverse the list order.
l2 = ["apple", "mango", "banana", "papaya", "kiwi", "pineapple", "banana"]
l2.reverse()
print(l2)

# `insert` method...
# insert an element at a specified position in a list.
num_list.insert(3, 666)  # 666 is inserted at the 3rd index position.
print(num_list)

# `pop` method...
# delete the last element from the list and return it.
popped_element = num_list.pop()
print(num_list)
print("Popped element:", popped_element)

# `remove` method...
# remove the first occurrence of a specified element from the list.
new_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]
new_list.remove(2)
print(new_list)

# NOTE: there are many more list methods in python. Check on ChatGPT.
