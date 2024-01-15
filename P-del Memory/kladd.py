import string
import random

def size_difficulty():
    #diff = int(input("Vill du spela med 3 bokstävers ord eller 4 bokstävers ord"))
    boardsize = int(input("Hur stor spelplan vill du ha? Svara endast en siffra brädan blir A * A"))

    return boardsize
def innershell(boardsize):
    winningboard=[]
    k = 0
    boardlist = []
    for i in range(boardsize):
        boardrow_list = []
        for j in range(1, boardsize+1):
            boardrow_list.append(string.ascii_uppercase[k] + str(j))
        boardlist.append(boardrow_list)
        k = k + 1
    return boardlist, winningboard
def print_board(memboard):
    numsizelist = []
    for l in range(1, boardsize+1):
        numsizelist.append(str(l)+ "\t")
    print("\t", *numsizelist)
    for num, currboard in enumerate(memboard, 0):
        print(string.ascii_uppercase[num], *currboard, sep="\t")
    return memboard


def outershell(boardsize):
    memboard = []
    for i in range(boardsize):
        row_list = []
        for j in range(1, boardsize+1):
            row_list.append("---")
        memboard.append(row_list)
    #print_board(memboard)
    return memboard
boardsize = size_difficulty()
boardlist = innershell(boardsize)

outershell(boardsize)
