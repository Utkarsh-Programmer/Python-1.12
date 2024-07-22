# Project 1
# Snake, Water, Gun Game

import random

# INSTRUCTIONS
"""
1 for snake
-1 for water
0 for gun
"""

# computer choice
computer = random.choice([-1, 0, 1])

# user choice
user_input = input("Enter your choice (s/w/g): ")

# user choice dictionary
user_dict = {
    "s": 1,
    "w": -1,
    "g": 0
}

# user choice reverse dictionary
reverse_dict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# user comparable choice
user_choice = user_dict[user_input]

# printing both choices
print(f"You chose: {reverse_dict[user_choice]}\nComputer chose: {
      reverse_dict[computer]}")

# game conditions
if computer == user_choice:
    print("It's a tie!")
else:
    # the logic below is based on the value of (computer - user_choice).
    if ((computer - user_choice == -1) or (computer - user_choice == 2)):
        print("You Lose!")
    else:
        print("You Win!")
