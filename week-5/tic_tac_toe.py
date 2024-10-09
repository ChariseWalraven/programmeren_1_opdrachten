# https://brightspace.hr.nl/d2l/lms/dropbox/user/folder_submit_files.d2l?db=53694&grpid=0&isprv=0&bp=0&ou=111528
# TODO: Use numpy 🤓
import numpy as np
from enum import StrEnum, IntEnum, auto


class UserInputError(ValueError):
    pass


# TODO: replace regular array interactions with numpy
# TODO: find winner

# TODO: replace with enums and emoji's 🤠
const_symbols = ["X", "O"]
const_board_size = (3, 3)


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
    introduction()
    return np.zeros(const_board_size)


def run_game(board):
    try:
        no_winner = True
        while no_winner:
            try:
                # take user input
                row, col, value = get_user_input()
                # play row
                board = update_board((row, col), value, board)
                print_board(board)
                print("winner? ", three_in_a_row(board))
            except UserInputError as e:
                print(e)
                continue
    except KeyboardInterrupt:
        print("\nQuit game.")


def introduction():
    print("Welcome to tic tac toe! To quit, press ctrl + c anytime.")


def get_user_input():
    row = int(input("Enter row: ")) - 1
    col = int(input("Enter column: ")) - 1
    value = input("Enter X or O (case insenstitive): ").upper()

    validate_user_input(row, col, value, board)

    return row, col, value


def validate_user_input(row, col, value, board):
    # BUG: can change cells that have already been played
    try:
        if board[row][col] in const_symbols:
            raise UserInputError("Position already taken, try another one.")
    except IndexError:
        raise UserInputError(
            "Invalid position entered, "
            "please enter a row and column number between 1 "
            f"and {len(const_board_size) + 1}"
        )

    if value not in const_symbols:
        raise UserInputError(
            'Invalid input, please enter either "X" or "O", '
            "no other symbols are permitted."
        )


def update_board(position, value, board):
    row, col = position
    board[row][col] = SymbolValues[value]

    return board


def print_board(board):
    def get_display_symbol(value):
        display = " "
        if value == SymbolValues.X:
            display = DisplaySymbols.X
        elif value == SymbolValues.O:
            display = DisplaySymbols.O
        return display

    print("  Board:", "=" * 9, sep="\n")
    for r in board:
        for c in r:
            display = get_display_symbol(c)
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
    board = init()
    print_board(board)
    run_game(board)
