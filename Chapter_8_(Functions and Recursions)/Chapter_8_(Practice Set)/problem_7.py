# Problem 7
# write a python function to remove a given word from a list and strip it at the same time.

l = ["Harry", "Sonam", "Sarthak", "ak", "Deepak"]


def rm_word(l, word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n


print(rm_word(l, "ak"))
