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
    if computer == -1 and user_choice == 1:
        print("You Win!")
    elif computer == -1 and user_choice == 0:
        print("You Lose!")

    elif computer == 1 and user_choice == -1:
        print("You Lose!")
    elif computer == 1 and user_choice == 0:
        print("You Win!")

    elif computer == 0 and user_choice == -1:
        print("You Win!")
    elif computer == 0 and user_choice == 1:
        print("You Lose!")
    else:
        print("Something Went Wrong.")
