def main():
    turn = 1
    win = False
    intro()
    player_1 = input("Who is player one? ")
    player_2 = input("Who is player two? ")
    row,col = size()
    board = game_board(row, col)

    while not win:
        board = update(board)
        board = inputs(board, row, turn, player_1, player_2)
        win = game_over(board)
        turn += 1

    print("\n" + "DONE!")
    if (turn % 2) == 1:
        print("\n" + player_2, "won!,",player_1, "sucks!!")
    else:
        print("\n" + player_1, "won!,",player_2, "sucks!!")
def game_over(board):
    if sum(len(x) for x in board) == 1:
        win = True
    else:
        win = False

    return win
def intro():
    print("Hello and welcome!")
    print("Play by choosing a number which will make all numbers to the right and below dissapear, player who eats 'P' loses.")
    print("Start by naming player one and player two")
def size():
    while True:
        try:
            row = int(input("How many rows? "))
            col = int(input("How many columns? "))
        except ValueError:
            print("Enter a number")
            continue
        except IndexError:
            print("Wrong input")
            continue
        if row > 9 or 2 > row:
            print("Pick a number between 1 and 9 for both rows and columns")
            continue
        if col > 9 or col < 2:
            print("Pick a number between 1 and 9 for both rows and columns")
            continue
        else:
            break
    return row, col
def game_board(rad_input, col):
    board = []
    row_size = 11
    col = col + 10
    for i in range(rad_input):
        row_list = []
        for j in range(row_size, col + 1):
            row_list.append(j)
        board.append(row_list)
        row_size = row_size + 10
        col = col + 10
    board[0][0] = "P "

    return board
def inputs(board, row, turn, player_1, player_2):
    play = True
    if (turn % 2) == 1:
        print(player_1,",", end=" ")
    else:
        print(player_2,",", end=" ")

    while play:
        try:
            choice = int(input("Where do you want to go?"))
        except ValueError:
            print("You have to go to an integer!")
            continue
        for rows in board:
            if choice in rows:
                play = False
        if play:
            print("Värdet är utanför spelplanen")


    for rows in board:
        for values in rows:
            if values == choice:
                x = rows.index(values)
                y = board.index(rows)
    while y < row:
        del board[y][x:]
        y += 1
    return board

def update(board):
    for row in board:
        for elem in row:
            print(elem, end=" ")
        print()
    return board

main()
