# https://brightspace.hr.nl/d2l/lms/dropbox/user/folder_submit_files.d2l?db=53694&grpid=0&isprv=0&bp=0&ou=111528
# TODO: Use numpy 🤓
import numpy as np
from enum import StrEnum, IntEnum, auto

# TODO: replace with enums and emoji's 🤠
const_symbols = ["X", "O"]


class StrSymbols(StrEnum):
    X = auto()
    O = auto()  # noqa: E741


class DisplaySymbols(StrEnum):
    X = "❎"
    O = "🅾️"  # noqa: E741


class SymbolValues(IntEnum):
    X = -1
    O = 1  # noqa: E741


def init():
    global board
    board = np.array([[0 for i in range(3)] for i in range(3)])
    introduction()


def run_game():
    try:
        no_winner = True
        while no_winner:
            # take user input
            # play row
            row, col, value = get_user_input()
            global board
            board = update_board((row, col), value, board)
            print_board(board)

    except KeyboardInterrupt:
        print("\nQuit game.")


def introduction():
    print("Welcome to tic tac toe! To quit, press ctrl + c anytime.")


def get_user_input():
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))
    value = input("Enter X or O (case insenstitive): ").upper()

    validate_user_input(row, col, value, board)

    return row, col, value


def validate_user_input(row, col, value, board):
    # row & col already taken?
    try:
        if board[row][col] in const_symbols:
            raise ValueError("Position already taken, try another one.")
    except IndexError:
        raise ValueError(
            "Invalid position entered, "
            "please enter a row and column number between 0 and 2"
        )

    if value not in const_symbols:
        raise ValueError(
            'Invalid input, please enter either "X" or "O", '
            "no other symbols are permitted."
        )


def update_board(position, value, board):
    row, col = position
    board[row][col] = SymbolValues[value]

    return board


def print_board(board):
    print("  Board:", "=" * 9, sep="\n")
    for r in board:
        for c in r:
            display = " "
            if c == SymbolValues.X:
                display = DisplaySymbols.X
            elif c == SymbolValues.O:
                display = DisplaySymbols.O

            print(
                "[",
                display,
                "]",
                sep="",
                end="",
            )
        print("", sep="")
    print("=" * 9)


def three_in_a_row(board):
    return any((sum(row) in {3, -3} for row in board))


if __name__ == "__main__":
    init()
    run_game()
