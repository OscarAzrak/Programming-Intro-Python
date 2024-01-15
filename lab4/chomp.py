"""
Chomp - a strategy game
"""

import random
import time

NUM_ROWS = 5
NUM_COLS = 6

def who_goes_first():
    print("Spelare 1 börjar!")


def play_again():
    print("Would you like to play again? (yes or no)")
    return input().lower().startswith("y")


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()


def validate_user_input(player_choice, board):
    try:
        row, col = player_choice.split()
    except ValueError:
        print("Bad input: The input should be exactly two numbers separated by a space.")
        return False
    try:
        row = int(row)
        col = int(col)
    except ValueError:
        print("Input must be two numbers, however non-digit characters were received.")
        return False

    if row < 0 or row > NUM_ROWS - 1:
        print(f"The first number must be between 0 and {NUM_ROWS - 1} but {row} was passed.")
        return False
    if col < 0 or col > NUM_COLS - 1:
        print(f"The second number must be between 0 and {NUM_COLS - 1} but {col} was passed.")
        return False
    if board[row][col] == " ":
        print("That square has already been eaten!")
        return False
    return True


def update_board(board, row, col):
    for i in range(row, len(board)):
        for j in range(col, len(board[i])):
            board[i][j] = " "


def get_human_move(board):
    valid_input = False
    while not valid_input:
        player_choice = input("Enter the row and column of your choice separated by a space: ")
        valid_input = validate_user_input(player_choice, board)
    row, col = player_choice.split()
    return int(row), int(col)


def get_player2_move(board):
    valid_input = False
    while not valid_input:
        player2_choice = input("Enter the row and column of your choice separated by a space: ")
        valid_input = validate_user_input(player2_choice, board)
    row, col = player2_choice.split()
    return int(row), int(col)


def main():
    board = []
    for i in range(NUM_ROWS):
        row = []
        for j in range(NUM_COLS):
            row.append("#")
        board.append(row)

    board[0][0] = "P"
    game_is_playing = True
    turn = "human"




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
                print("Too bad, the spelare 2 wins!")
                game_is_playing = False
            else:
                update_board(board, row, col)
                print()
                print_matrix(board)
                print()
                turn = "spelare 2"
                time.sleep(1)
        else:
            # Computer turn
            row, col = get_player2_move(board)
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

    if play_again():
        main()
    else:
        print("Goodbye!")
        raise SystemExit


main()