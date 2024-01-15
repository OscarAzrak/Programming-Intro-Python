"""
Chomp - a strategy game
"""

import random
import time
EMPTY_SPOT = " "
NUM_ROWS = 5
NUM_COLS = 6


def print_title():
    print(r"""
 ______     __  __     ______     __    __     ______  
/\  ___\   /\ \_\ \   /\  __ \   /\ "-./  \   /\  == \ 
\ \ \____  \ \  __ \  \ \ \/\ \  \ \ \-./\ \  \ \  _-/ 
 \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \ \_\  \ \_\   
  \/_____/   \/_/\/_/   \/_____/   \/_/  \/_/   \/_/   
""")


def print_instructions():
    print("Welcome to Chomp. Choose a square and all squares to the right")
    print("and downwards will be eaten. The computer will do the same.")
    print("The one to eat the poison square loses. Good luck!")
    print()


def who_goes_first():
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "human"


def play_again():
    print("Would you like to play again? (yes or no)")
    return input().lower().startswith("y")


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))


def validate_user_input(player_choice, board):
    try:
        row, col = player_choice.split()
    except ValueError:
        raise ValueError(
            "Bad input: The input should be exactly two numbers separated by a space."
        )

    try:
        row = int(row)
        col = int(col)
    except ValueError:
        raise ValueError(
            "Input must be two numbers, however non-digit characters were received."
        )

    if row < 0 or row > NUM_ROWS - 1:
        raise ValueError(
            f"The first number must be between 0 and {NUM_ROWS - 1} but {row} was passed."
        )

    if col < 0 or col > NUM_COLS - 1:
        raise ValueError(
            f"The second number must be between 0 and {NUM_COLS - 1} but {col} was passed."
        )

    if board[row][col]  " ":
        raise ValueError("That square has already been eaten!")

    return row, col


def get_human_move(board):
    while True:
        player_choice = input("Enter the row and column of your choice separated by a space: ")
        try:
            row, col = validate_user_input(player_choice, board)
            break
        except ValueError as ex:
            print(ex)
    return row, col


def update_board(board, row, col):
    for i in range(row, len(board)):
        for j in range(col, len(board[i])):
            board[i][j] = " "




def get_computer_move(board):
    while True:
        row = random.randint(0, NUM_ROWS - 1)
        col = random.randint(0, NUM_COLS - 1)
        if board[row][col] == EMPTY_SPOT:
            continue
        else:
            break
    return row, col


def main():
    board = [["#" for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

    board[0][0] = "P"
    game_is_playing = True
    turn = "human"

    print_title()
    print_instructions()

    while game_is_playing:
        if turn == "human":
            # Human turn
            print("Human turn.")
            print()
            print_matrix(board)
            print()
            row, col = get_human_move(board)
            if board[row][col] == "P":
                print()
                print("Too bad, the computer wins!")
                game_is_playing = False
            else:
                update_board(board, row, col)
                print()
                print_matrix(board)
                print()
                turn = "computer"
                time.sleep(1)
        else:
            # Computer turn
            row, col = get_computer_move(board)
            print(f"Computer turn. the computer chooses ({row}, {col})")
            print()
            if board[row][col] == "P":
                print()
                print("Yay, you win!")
                game_is_playing = False
            else:
                update_board(board, row, col)
                print_matrix(board)
                print()
                turn = "human"

        if not play_again():
            print("Goodbye!")
            break


main()