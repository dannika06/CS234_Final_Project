"""
A simple dice rolling simulator that generates a random number between 1 and 6.
"""

import random


def roll_dice() -> int:
    """
    Rolls a dice and returns a random number between 1 and 6.
    """
    dice_number = random.randint(1, 6)
    return dice_number


print("===== Welcome to Dice Rolling Simulator =====")
while 1:
    choice = input("Do you wanna roll a dice (y/n)")
    if "y" in choice.lower():
        print("Rolling dice...")
        number = roll_dice()
        print("Dice has the number:", number)
    elif "n" in choice.lower():
        print("Exiting...")
        break
    else:
        print("Invalid input...please try again")
