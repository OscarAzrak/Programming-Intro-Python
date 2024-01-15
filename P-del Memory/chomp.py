def main():
    tur = 1
    vinst = False
    intro()
    spelare_1 = input("Vem spelar först? ")
    spelare_2 = input("Vem är andra spelaren? ")
    rad,col = utseende()
    board = spelbrada(rad, col)

    while not vinst:
        board = update(board)
        board = matain(board, rad, tur, spelare_1, spelare_2)
        vinst = spelslut(board)
        tur += 1

    print("\n" + "SLUT!")
    if (tur % 2) == 1:
        print("\n" + spelare_2, "vann,",spelare_1, "suger!!")
    else:
        print("\n" + spelare_1, "vann,",spelare_2, "suger!!")
def spelslut(board):
    if sum(len(x) for x in board) == 1:
        vinst = True
    else:
        vinst = False

    return vinst
def intro():
    print("Hej välkomna!")
    print("Dags för lite chomp kära vänner")
    print("Spela genom att välja en siffra, vilket kommer göra att alla siffror åt höger och under försvinner, den spelaren som 'äter' P förlorar.")
    print("Börja med att tala om vem som spelar och sedan hur eran spelplan ska se ut!")
def utseende():
    while True:
        try:
            rad = int(input("hur många rader? "))
            col = int(input("hur många kolumner ska spelet vara? "))
        except ValueError:
            print("Skriv med siffror")
            continue
        except IndexError:
            print("Nej")
            continue
        if rad > 9 or 2 > rad:
            print("Ange en siffra mellan 1 och 9 på både rad och kolumner! ")
            continue
        if col > 9 or col < 2:
            print("Ange en siffra mellan 1 och 9 på både rad och kolumner! ")
            continue
        else:
            break
    return rad, col
def spelbrada(rad, col):
    board = []
    row = 11
    col = col + 10
    for i in range(rad):
        row_list = []
        for j in range(row, col + 1):
            row_list.append(j)
        board.append(row_list)
        row = row + 10
        col = col + 10
    board[0][0] = "P "
    return board
def matain(board, rad, tur, spelare_1, spelare_2):
    spela = True
    if (tur % 2) == 1:
        print(spelare_1,",", end=" ")
    else:
        print(spelare_2,",", end=" ")

    while spela:
        try:
            val = int(input("var vill du gå?"))
        except ValueError:
            print("Du måste gå till ett heltal")
            continue
        for a in board:
            if val in a:
                spela = False
        if spela:
            print("Värdet är utanför spelplanen")


    for l in board:
        for i in l:
            if i == val:
                x = l.index(i)
                y = board.index(l)
    while y < rad:
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
