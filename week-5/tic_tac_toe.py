# https://brightspace.hr.nl/d2l/lms/dropbox/user/folder_submit_files.d2l?db=53694&grpid=0&isprv=0&bp=0&ou=111528
import numpy as np

from enum import StrEnum, IntEnum
from playsound3 import playsound


# region - errors & enums
class UserInputError(ValueError):
    pass


class StrSymbols(StrEnum):
    X = "X"
    O = "O"  # noqa: E741


class DisplaySymbols(StrEnum):
    X = "❎"
    O = "🅾️"  # noqa: E741


class SymbolValues(IntEnum):
    X = -1
    O = 1  # noqa: E741


class SfxUrls(StrEnum):
    __base_url__ = "https://raw.githubusercontent.com/ChariseWalraven/tic_tac_toe_sfx/refs/heads/main"  # noqa: E501
    player_win = f"{__base_url__}/player_win.mp3"
    player_lose = f"{__base_url__}/player_lose.mp3"
    player_draw = f"{__base_url__}/player_draw.mp3"


# endregion


# region - constants
const_symbol_strings = [s.value for s in StrSymbols]
const_symbol_values = [s.value for s in SymbolValues]
const_board_display_symbols = [
    "1️⃣ ",
    "2️⃣ ",
    "3️⃣ ",
    "4️⃣ ",
    "5️⃣ ",
    "6️⃣ ",
    "7️⃣ ",
    "8️⃣ ",
    "9️⃣ ",
]
# endregion - constants

# region - config
config_board_size = (3, 3)
config_player_symbol = None
config_bot_symbol = None
# endregion


# region - lib methods
def get_symbol_string_from_input(input):
    str_symbol = [symbol for symbol in StrSymbols if symbol == input]
    return str_symbol[0] if len(str_symbol) > 0 else None


def allow_quitting(game_loop_fn):
    """Decorator. When user presses ctrl + c, prints message confirming
    that game has quit.
    Meant to be used with game loop to avoid nesting from
    try...except statements.
    """

    def inner_fn(*args):
        try:
            game_loop_fn(*args)
        except KeyboardInterrupt:
            print("\nQuit game.")

    return inner_fn


def clear_screen():
    print("\033c")


# endregion


# region - general methods
def init():
    introduction()
    set_player_symbol()
    set_bot_symbol()
    return np.zeros(config_board_size)  # init board


def introduction():
    print("Welcome to tic tac toe! To quit, press ctrl + c anytime.")


def get_turn(player_turn, board):
    if player_turn:
        print("Your play:")
        value = config_player_symbol.value
        # take user input
        row, col = get_user_input(board)
        player_turn = False
    else:
        # get bot input
        row, col = get_bot_play(board)
        value = config_bot_symbol.value
        player_turn = True
    return row, col, value, player_turn


@allow_quitting
def run_game(board):
    winner = False
    draw = False
    player_turn = True
    print("Player goes first.")
    while not winner and not draw:
        row, col, value = (None, None, None)
        try:
            row, col, value, player_turn = get_turn(player_turn, board)
        except UserInputError as e:
            print(e)
            continue
        # play row
        clear_screen()
        bot_display_symbol = DisplaySymbols[config_bot_symbol]
        (
            print(
                f"Bot played an {bot_display_symbol}",
                f"in position: {get_pos_from_row_col(row, col, board)}",
            )
            if player_turn
            else None
        )
        board = update_board((row, col), value, board)
        print_board(board)

        winner = check_winner(board)
        draw = check_draw(board)
    else:
        if winner and not player_turn:
            print("Congratulations, you won!")
            playsound(SfxUrls.player_win)
        elif winner and player_turn:
            print("Beaten by the bot! Surrender to your robot overlords! 🤖")
            playsound(SfxUrls.player_lose)
        elif draw:
            print("It's a draw. Better luck next time.")
            playsound(SfxUrls.player_draw)


# endregion


# region - bot methods
def get_bot_play(board):
    # get list of free spots
    free_cells = np.argwhere(board == 0)
    # pick a random coordinate from the list of untaken coordinates
    play_idx = np.random.choice(free_cells.shape[0], 1)
    play = free_cells[play_idx][0]
    # choose one
    return play


def set_bot_symbol():
    global config_player_symbol, config_bot_symbol
    # get remaining symbol
    config_bot_symbol = [s for s in StrSymbols if s != config_player_symbol][0]


# endregion


# region - user input & input validation methods
def set_player_symbol():
    global config_player_symbol
    symbol = input("Choose a symbol: enter 'X' or 'O'").upper()
    validate_user_symbol(symbol)
    config_player_symbol = get_symbol_string_from_input(symbol)


def get_user_input(board):
    position = input("Enter position: ")
    validate_user_position(position)
    row, col = get_row_col_from_pos(int(position), board)
    validate_user_input(row, col, board)

    return row, col


def get_row_col_from_pos(position: int, board):
    coord = np.argwhere(board > -2)[position - 1]

    return coord[0], coord[1]


def get_pos_from_row_col(row: int, col: int, board):
    return (col + row * 3) + 1


def validate_user_input(row: str, col: str, board):

    try:
        if board[row][col] in const_symbol_values:
            raise UserInputError("Position already taken, try another one.")
    except IndexError:
        raise UserInputError(
            "Invalid position entered, "
            "please enter a row and column number between 1 "
            f"and {len(config_board_size) + 1}"
        )


def validate_user_symbol(symbol):
    if symbol not in const_symbol_strings:
        raise UserInputError(
            'Invalid input, please enter either "X" or "O", '
            "no other symbols are permitted."
        )


def validate_user_position(pos: str):
    """
    Raises a UserInputError if the position is not an integer or
    is out of bounds
    """
    try:
        pos = int(pos)
        assert pos > 0 and pos < 10
    except (AssertionError, ValueError):
        raise UserInputError(
            "Invalid row or column position.",
        )


# endregion


# region - board methods
def print_board(board):
    def get_display_symbol(value, pos):
        display = const_board_display_symbols[pos - 1]
        if value == SymbolValues.X:
            display = DisplaySymbols.X
        elif value == SymbolValues.O:
            display = DisplaySymbols.O
        return display

    print("  Board:", "=" * 9, sep="\n")
    for r_i, r in enumerate(board):
        for c_i, c in enumerate(r):
            pos = get_pos_from_row_col(r_i, c_i, board)
            display = get_display_symbol(c, pos)
            print(
                "[",
                display,
                "]",
                sep="",
                end="",
            )
        print("", sep="")
    print("=" * 9)


def update_board(position, value, board):
    row, col = position
    board[row][col] = SymbolValues[value]

    return board


# endregion


# region - victory methods
def check_winner(board):
    row_winner = three_in_a_row(board)
    diagonal_winner = three_in_a_row(
        np.array(
            [
                np.diagonal(np.fliplr(board)).tolist(),
                np.diagonal(board).tolist(),
            ]
        )
    )
    col_winner = three_in_a_row(np.rot90(board))
    return row_winner or col_winner or diagonal_winner


def check_draw(board):
    # if no more free spaces then it's a draw
    return len(np.argwhere(board == 0)) == 0


def three_in_a_row(board):
    sums = (sum(row) in {3, -3} for row in board)
    return any(sums)


# endregion


@allow_quitting
def main():
    playing = True
    while playing:
        board = init()
        print_board(board)
        run_game(board)
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "n":
            playing = False


if __name__ == "__main__":
    main()
