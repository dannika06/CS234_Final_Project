"""
A simple Tic Tac Toe game for two players."""
import sys


board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
X = "X"
O = "O"


def display_board() -> None:
    """
    Displays the current state of the Tic Tac Toe board.
    """
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" ----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" ----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")


def update_board(character: str, position: int) -> None:
    """
    Updates the board with the given character at the specified position.
    Args:
        character (str): The character to place on the board ('X' or 'O').
        position (int): The position on the board (1-9).
    Returns:
        None
    """
    row = (position - 1) // 3
    column = (position - 1) % 3
    board[row][column] = character


def check_win() -> int:
    """
    Checks if there is a winner on the board.
    Returns 1 if there is a winner, otherwise returns 0.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return 1
        if board[0][i] == board[1][i] == board[2][i]:
            return 1

    if board[0][2] == board[1][1] == board[2][0]:
        return 1
    if board[0][0] == board[1][1] == board[2][2]:
        return 1
    return 0


def check_position(position: int) -> int:
    """
    Checks if the given position on the board is available.
    Args:
        position (int): The position on the board (1-9).
    Returns:
        int: 1 if the position is available, 0 if it is already occupied.
    """
    row = (position - 1) // 3
    column = (position - 1) % 3
    if board[row][column] == X or board[row][column] == O:
        return 0
    return 1


print("===== Welcome to Tic Tac Toe Game =====")
counter = 0
while 1:
    if counter % 2 == 0:
        display_board()
        while 1:
            choice = int(
                input(f"Player {(counter % 2)+1}, "
                      f"enter your position ('{X}'): ")
            )
            if choice < 1 or choice > 9:
                print("Invalid input...please try again.")
            if check_position(choice):
                update_board(X, choice)
                if check_win():
                    print(f"Conguratulations !!! "
                          f"Player {(counter % 2)+1} won !!!")
                    sys.exit(0)
                else:
                    counter += 1
                    break
            else:
                print(
                    f"Position {choice} is already occupied."
                    f" Choose another position."
                )
        if counter == 9:
            print("The match ended with a draw !!! Better luck next time")
            sys.exit(0)
    else:
        display_board()
        while 1:
            choice = int(
                input(f"Player {(counter % 2)+1},"
                      f" enter your position ('{O}'): ")
            )
            if choice < 1 or choice > 9:
                print("Invalid input...please try again.")
            if check_position(choice):
                update_board(O, choice)
                if check_win():
                    print(f"Conguratulations !!!"
                          f"Player {(counter % 2)+1} won !!!")
                    sys.exit(0)
                else:
                    counter += 1
                    break
            else:
                print(
                    f"Position {choice} is already occupied."
                    f" Choose another position."
                )
    print()
