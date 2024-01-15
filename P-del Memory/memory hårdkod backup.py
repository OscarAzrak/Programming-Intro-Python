import random
import time
import string


def innershell():
    winningboard=[]
    k = 0
    boardlist = []
    for i in range(7):
        boardrow_list = []
        for j in range(1, 8):
            boardrow_list.append(string.ascii_uppercase[k-1] + str(j-1))
        boardlist.append(boardrow_list)
        k = k + 1
    return boardlist, winningboard


def main():
    vinst = False
    turn = 1
    boardlist, winningboard = innershell()
    memboard = outershell()
    answer = importmemo3()
    #y1, nx1, my2, nx2 = hej()
    #print(answer)

    while not vinst:
        showboard(memboard)
        choice(boardlist, turn, answer, winningboard)
        vinst = spelslut(winningboard)
        turn += 1


def spelslut(winningboard):
    if len(winningboard) == 18:
        vinst = True
    else:
        vinst = False
    return vinst

def choice(boardlist,turn,answer,winningboard):
    spela = True
    print("Val",turn,":", end=" ")
    while spela:
        val1 = input("var vill du gå?").upper()
        for a in boardlist:
            if val1 in a:
                spela = False
        if spela:
            print("Värdet finns inte spelplanen")
    for l in boardlist:
        for i in l:
            if i == val1:
                nx1 = l.index(i)
                my1 = boardlist.index(l)

    nx1 = nx1
    my1 = my1
    print(my1,nx1)

    show_choice(answer, memboard, (my1, nx1))
    val2 = input("var?").upper()
    for a in boardlist:
        if val1 and val2 in a:
            spela = False
        if spela:
            print("Värdet finns inte spelplanen")
        #if answer[my2][nx2] in winningboard:
        #    print("Du har redan valt denna platta!")
        #    continue
        #else:
        #    pass

    for K in boardlist:
        for i in K:
            if i == val2:
                nx2 = K.index(i)
                my2 = boardlist.index(K)
    nx2 = nx2
    my2 = my2
    print(answer[my2-1][nx2-1])
    show_choice(answer, memboard, (my1, nx1),(my2,nx2))
    if answer[my1-1][nx1-1] == answer[my2-1][nx2-1]:
        print('Samma!')
        memboard[my1][nx1] = answer[my1-1][nx1-1]
        memboard[my2][nx2] = answer[my2-1][nx2-1]
        winningboard.append(answer[my1-1][nx1-1])
    else:
        print('Tyvärr, de var ej samma.')
    #print(answer)
    print(winningboard)
    return memboard,winningboard, my1, nx1, my2, nx2

def show_choice(answer,memboard,*tiles):
    for row in range(len(memboard)):
        for column in range(len(memboard[0])):
            if (row, column) in tiles:
                print(answer[row-1][column-1], end='   ', flush=True)
            else:
                print(memboard[row][column], end='   ', flush=True)
        print()


def importmemo3():
    randlists = []
    infile = open("memory3.txt", "r")
    for line in infile:
        randlists.append(line.replace("\n", ""))
    infile.close()

    rand_options = randlists
    answer = []
    for _ in range(18):
        rand_list = random.choice(rand_options)
        answer.append(rand_list)
        rand_options.remove(rand_list)
    answer = 2*answer
    random.shuffle(answer)
    answer = [answer[:6],
              answer[6:12],
              answer[12:18],
              answer[18:24],
              answer[24:30],
              answer[30:]]
    return answer
#rand_lists är den som har alla random ord

#def answers():

def outershell():
    global memboard
    memboard = []
    for i in range(7):
        row_list = []
        for j in range(1, 8):
            row_list.append(" - ")
        memboard.append(row_list)
    memboard[0][0] = " "
    # ändrar första elementen till vänster om matrisen till 1,2,3...
    y = 0
    while y < 6:
        memboard[y + 1][0] = string.ascii_uppercase[y]
        y += 1
    # ändrar högst upp i matrisen till 1,2,3...
    x = 1
    while x < 7:
        memboard[0][x] = (" "+str(x)+" ")
        x += 1
    return memboard

def updateboard():

    pass

def showboard(memboard):
    for o in memboard:
        for elem in o:
            print(elem, end="   ")
        print()
main()
