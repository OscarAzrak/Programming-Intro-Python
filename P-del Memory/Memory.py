import random
import time
import string
import copy
#import memoryclass


class Game: #Skapar class "Game" för att kolla när spelet tar slut
    def __init__(self, Word):
        self.__Word = Word
        self.__isCompleted = False  # insatn
        self.__isHidden = True
        self.AmountShown = 0
    def __str__(self):
        if self.__isHidden:
            return "---"
    def isHidden(self):
        return self.__isHidden
    def isCompleted(self):
        return self.__isCompleted


def innershell(boardsize):
    winningboard = [] #ord som blir rätt svar läggs in i denna lista
    k = 0
    boardchoice = [] # lista med alternativen A1,A2, A3 osv
    for i in range(boardsize):
        boardrow_list = []
        for j in range(1, boardsize+1):
            boardrow_list.append(string.ascii_uppercase[k] + str(j)) # lägger till string A+ string 1 = A1 exempel
        boardchoice.append(boardrow_list) #Lägger till hela A1, A2, A3, A4... listan i en lista i boardchoice
        k = k + 1 #k ökar så att string.ascii_uppercase[k] gär från A till ,beroende på hur stor bräda man valt, den bokstav som är sist
    return boardchoice, winningboard


def main():
    vinst = False
    turn = 1
    boardsize, boardsizehalf = size_difficulty()
    boardlist, winningboard = innershell(boardsize)
    memboard = outershell(boardsize)
    answer = importmemo3(boardsizehalf, boardsize)
    while not vinst:
        print_board(memboard, boardsize)
        choice(boardlist, turn, answer, winningboard,memboard, boardsize)
        vinst = spelslut(winningboard, boardsize)
        turn += 1

def size_difficulty():
    #diff = int(input("Vill du spela med 3 bokstävers ord eller 4 bokstävers ord"))
    boardsize = int(input("Hur stor spelplan vill du ha? Svara endast en siffra brädan blir A * A"))
    boardsizehalf = int(0.5*boardsize*boardsize)

    return boardsize, boardsizehalf

def print_board(memboard, boardsize):
    numsizelist = []
    for l in range(1, boardsize+1):
        numsizelist.append(str(l)+ "\t")
    print("\t", *numsizelist)
    for num, currboard in enumerate(memboard, 0):
        print(string.ascii_uppercase[num], *currboard, sep="\t")
    return memboard

def spelslut(winningboard, boardsizehalf): #Funkar bara för för 4x4
    print(len(winningboard))
    if 0.5*len(winningboard) == boardsizehalf: #när winningboard innehåller ett av antal ord från spelet är spelet slut
        vinst = True
    else:
        vinst = False
    return vinst

def choice(boardlist,turn,answer,winningboard, memboard, boardsize):
    spela = True
    print("Val",turn,":", end=" ")
    while spela:
        val1 = input("var vill du gå?").upper() #oavsett om man skriver litet a eller stort A blir input automatiskt stort A för att känna igen i boardchoice listan
        for a in boardlist:
            if val1 in a:
                spela = False
        if spela:
            print("Värdet finns inte spelplanen")
    for l in boardlist:
        for i in l:
            if i == val1:
                nx1 = l.index(i) #ger platsen(index) i X-led på vart val1 ligger i listorna
                my1 = boardlist.index(l) #ger platsen(index) i Y-led på vart val1 ligger i listorna

    print(my1,nx1) #Bara för att se att allt stämmer, ta bort sen

    show_choice(boardsize, answer, memboard, (my1, nx1))
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

    print(answer[my2][nx2])
    show_choice(boardsize, answer, memboard, (my1, nx1),(my2,nx2))
    if answer[my1][nx1] == answer[my2][nx2]: #ifall andra och första valet ger samma ord så sparas det ordet kvar och inte längre är det streck
        print('Samma!')
        memboard[my1][nx1] = answer[my1][nx1] #ändrar från streck till ord
        memboard[my2][nx2] = answer[my2][nx2]
        winningboard.append(answer[my1][nx1])
    else:
        print('Tyvärr, de var ej samma.')
    #print(answer)
    print(winningboard) #bara för att se ifall det funkar, ta bort sen
    return memboard,winningboard, my1, nx1, my2, nx2

def show_choice(boardsize, answer,memboard,*tiles):
    print(len(answer)) #ta bort sen
    tempmemboard = copy.deepcopy(memboard)
    for row in range(len(memboard)):
        for column in range(len(memboard[0])):
            if (row, column) in tiles:
                tempmemboard[row][column] = answer[row][column]
                print_board(tempmemboard, boardsize)
                #print(answer[row][column], end='   ', flush=True)
            #else:
                #tempmemboard = memboard
                #print(memboard[row][column], "hej", end='   ', flush=True)
def divide_answerlist(anslist, size):
    # loopar längden till listan
    for i in range(0, len(anslist), size):
        yield anslist[i:i + size]


def importmemo3(boardsizehalf, boardsize):
    randlists = [] #tom lista där alla ord från hela memory3.txt filen läggs in
    infile = open("memory3.txt", "r")
    for line in infile:
        randlists.append(line.replace("\n", "")) #lägger in alla ord samt tar bort \n och byter ut mot ingenting, vilket gör att de går bort.
    infile.close() #stänger infilen
    answer_row=[]   #Listan med alla ord som ska vara AxA
    for _ in range(boardsizehalf): #väljer antal rader beroende på hur stor spelbräda man har
        rand_list = random.choice(randlists)
        answer_row.append(rand_list)
    answer_row = 2*answer_row
    random.shuffle(answer_row)
    answer = list(divide_answerlist(answer_row, boardsize))
    return answer
#rand_lists är den som har alla random ord

#def answers():

def outershell(boardsize):
    memboard = []    #tomlista där  - - -  osv läggs in beroende på hur stor bräda man vill ha
    for i in range(boardsize):
        row_list = []
        for j in range(1, boardsize + 1):
            #row_list.append("---") #just nu är det 3 streck, ändra till variabel som beror på hur långa ord man vill ha.
            row_list.append(Game(True))
        memboard.append(row_list)
    #print_board(memboard, boardsize)
    return memboard

def updateboard():

    pass

def showboard(memboard):
    for o in memboard:
        for elem in o:
            print(elem, end="   ")
        print()
main()
