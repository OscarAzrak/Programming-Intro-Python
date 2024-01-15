import random
import time

N_rad = int(input("Hur många rader ska spelet ha? "))
N_kol = int(input("Hur många kollumner ska spelet ha? "))

def vem_startar():
    if random.randint(0, 1) == 0:
        return "Spelare 1"
    else:
        return "Spelare 2"

def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()

def bekr_spelare1_vad(spelare1_val, plan):
    try:
        rad, kol = spelare1_val.split()
    except ValueError:
        print("Fel val, måste vara ett nummer som finns i spelplanen. ")
        return False
    try:
        rad = int(rad)
        kol = int(kol)
    except ValueError:
        print("Input must be two numbers, however non-digit characters were received.")
        return False

    if rad < 0 or rad > N_rad - 1:
        print(f"The first number must be between 0 and {N_rad - 1} but {rad} was passed.")
        return False
    if kol < 0 or kol > N_kol - 1:
        print(f"The second number must be between 0 and {N_kol - 1} but {kol} was passed.")
        return False
    if plan[rad][kol] == " ":
        print("Det nummret har redan blivit tagen!")
        return False
    return True

def uppdatera_plan(plan, rad, kol):
    for i in range(rad, len(plan)):
        for j in range(kol, len(plan[i])):
            plan[i][j] = " "

def spelare_1_drag(plan):
    valid_input = False
    while not valid_input:
        spelare1_val = input("Enter the row and column of your choice separated by a space: ")
        valid_input = bekr_spelare1_vad(spelare1_val, plan)
    rad, kol = spelare1_val().split()
    return int(rad), int(kol)

def get_computer_move(plan):
    valid_move = False
    while not valid_move:
        rad = random.randint(0, N_rad - 1)
        kol = random.randint(0, N_kol - 1)
        if plan[rad][kol] == " ":
            continue
        else:
            valid_move = True
    return rad, kol

def main():
    board = []
    for i in range(N_rad):
        row = []
        for j in range(N_kol):
            row.append("#")
        board.append(row)

    board[0][0] = "P"
    game_is_playing = True
    tur = "spelare 1"

    while game_is_playing:
        if tur == "spelare 1":
            # Human turn
            print("spelare 1 tur.")
            print()
            print_matrix(board)
            print()
            rad, kol = spelare_1_drag(plan)
            if plan[rad][kol] == "P":
                print()
                print("Too bad, the computer wins!")
                game_is_playing = False
            else:
                uppdatera_plan(plan, rad, kol)
                print()
                print_matrix(plan)
                print()
                turn = "computer"
                time.sleep(1)
        else:
            # Computer turn
            rad, kol = get_computer_move(board)
            print(f"Computer turn. the computer chooses ({rad}, {kol})")
            print()
            if board[rad][kol] == "P":
                print()
                print("Yay, you win!")
                game_is_playing = False
            else:
                uppdatera_plan(plan, rad, kol)
                print_matrix(board)
                print()
                tur = "human"



main()