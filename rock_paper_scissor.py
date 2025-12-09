"""
A simple Rock, Paper, Scissor game where the user plays against the computer.
"""

import random

ROCK = "rock"
PAPER = "paper"
SCISSOR = "scissor"
choices = [ROCK, PAPER, SCISSOR]
positive = [[PAPER, ROCK], [SCISSOR, PAPER], [ROCK, SCISSOR]]
negative = [[ROCK, PAPER], [PAPER, SCISSOR], [SCISSOR, ROCK]]


def get_computer_move() -> str:
    """
    Randomly selects and returns the computer's move.
    choices = [ROCK, PAPER, SCISSOR]
    """
    return random.choice(choices)


def find_winner(user_move: str, computer_move: str) -> int:
    """
    Determines the winner of the game.
    Returns 1 if user wins, -1 if computer wins, and 0 for a tie.
    """
    if [user_move, computer_move] in positive:
        return 1
    if [user_move, computer_move] in negative:
        return -1
    return 0


print("===== Welcome to Rock, Paper And Scissor Game =====")
while True:
    choice = input("Do you wanna play (y/n): ").strip().lower()
    if choice == "y":
        computers_move = get_computer_move()
        while True:
            move = (
                input("Select a move ('r' for rock/'p' for paper/'s' for scissor): ")
                .strip()
                .lower()
            )
            if move in ["r", "p", "s"]:
                users_move = {"r": ROCK, "p": PAPER, "s": SCISSOR}[move]
                print(f"User Move: {users_move}")
                print(f"Computer's Move: {computers_move}")
                output = find_winner(users_move, computers_move)
                if output == 1:
                    print("User Won !!!")
                elif output == -1:
                    print("Computer Won !!!")
                else:
                    print("It's a Tie !!!")
                break
            print("Invalid input...please try again")
    elif choice == "n":
        print("Exiting... Thanks for playing!")
        break
    else:
        print("Invalid input...please try again")
    print()
