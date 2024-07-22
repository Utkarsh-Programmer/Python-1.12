# Project 12
# The Perfect Guess

import random
from random import randint

# winning number
win_num = randint(1, 100)

print(win_num)

# game is not over
game_over = False

# total guesses
guesses = 0

# game runs when the game is not over
while not game_over:
    # user guess
    num = int(input("Guess the number: "))
    guesses += 1  # number of guesses increase by 1 each time the user enters a guess

    # game conditions
    if num > win_num:
        print("Too High!")
    elif num < win_num:
        print("Too Low!")
    else:
        game_over = True
        print(f"You have guessed the number {win_num} in {guesses} attempts.")
