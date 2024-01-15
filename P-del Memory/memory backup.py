import random
import string
import copy
class Game: #Skapar class "Game" för att kolla när spelet tar slut
    def __init__(self, Word):
        self.__Word = Word
        self.__isCompleted = False  # insatn
        self.__isHidden = True

    def __str__(self):
        if self.__isHidden:
            return f"---" #formatera strängar inom python
        else:
            return self.__Word
    def isHidden(self):
        return self.__isHidden
    def isCompleted(self):
        return self.__isCompleted
    def setBoxIsNotHiddenAnymore(self):
        self.__isHidden = False
    def setBoxIsCompleted(self):
        self.__isCompleted = True



def sizeOfGame(): #asks user for width and length of the field and also how many bombs to be included in the game. Returns correct values due to input-checks.
    boardsizeOK = False

    minValue = 2 #minst 2, jämna tal oxå
    while boardsizeOK == False:
        print("Vad ska storleken på brädan vara? Storleken är AxA, välj endast A? (A: ")
        boardsize = input()
        boardsizeOK = checkInputOK(boardsize, minValue)
    boardsizehalf = int((int(boardsize)**2)/2)
    return int(boardsize), boardsizehalf
def checkInputOK(value, minValue): #Funktion som kollar om banans storlek är korrekt
    okInput = False
    try:
        value = int(value)
        if value >= minValue:
            okInput = True
        else:
            print("Value should be in atleast 2:")
    except ValueError:
        print("Wrong input. Type in an integer.")
    return okInput

def randomwords(boardsize, boardsizehalf): #Function som hämtar ord från txt fil och väljer random ord
    randlists = [] #tom lista där alla ord från hela memory3.txt filen läggs in
    infile = open("memory3.txt", "r")
    for line in infile:
        randlists.append(line.replace("\n", "")) #lägger in alla ord samt tar bort \n och byter ut mot ingenting, vilket gör att de går bort.
    infile.close() #stänger infilen
    answer_row=[]   #Listan med alla ord som ska delas upp till AxA
    for _ in range(boardsizehalf): #väljer antal rader beroende på hur stor spelbräda man har
        rand_list = random.choice(randlists) #tar ett random ord och lägger in det i rand_list, i boardsizehalf antal gånger
        answer_row.append(Game(rand_list))
    answer_row = 2*answer_row
    random.shuffle(answer_row)
    answer = list(divide_answerlist(answer_row, boardsize))
    #print(len(answer))
    #print(len(answer[0]))
    return answer

def divide_answerlist(anslist, size):
    # loopar längden till listan
    for i in range(0, len(anslist), size):
        yield anslist[i:i + size]

def createBoard(boardsize):
    boardshow = []    #tomlista där  - - -  osv läggs in beroende på hur stor bräda man vill ha
    for i in range(boardsize):
        row_list = []
        for j in range(1, boardsize + 1):
            #row_list.append("---") #just nu är det 3 streck, ändra till variabel som beror på hur långa ord man vill ha.
            row_list.append(Game(True))
        boardshow.append(row_list)
    return boardshow

def createSelectBoard(boardsize):
    k = 0
    BoardSelect = [] # lista med alternativen A1,A2, A3 osv
    for i in range(boardsize):
        BoardSelectRow_list = []
        for j in range(1, boardsize+1):
            BoardSelectRow_list.append(string.ascii_uppercase[k] + str(j)) # lägger till string A+ string 1 = A1 exempel
        BoardSelect.append(BoardSelectRow_list) #Lägger till hela A1, A2, A3, A4... listan i en lista i boardchoice
        k = k + 1 #k ökar så att string.ascii_uppercase[k] gär från A till ,beroende på hur stor bräda man valt, den bokstav som är sist
    return BoardSelect

def Print_Board(answer):
    for i in range(1, len(answer[0]) + 1):
        print("\t", i, end=" ")
    print()
    for index, row in enumerate(answer):
        print(string.ascii_uppercase[index], end="\t")
        for box in row:
            print(box, end="\t")
        print()

def getCoordinates(turn, boardsize, answer): #a function that asks for and makes sure user input-coordinates are correct.
    CoordinatesOK = False
    print("val", turn, ":")
    while CoordinatesOK == False:
        val1 = input("var vill du gå?").upper() #oavsett om man skriver litet a eller stort A blir input automatiskt stort A för att känna igen i boardchoice listan
        val1 = val1.lower()
        try:
            row = val1[:1]
            column = int(val1[1:])
            for character in row:
                row_number = ord(character) - 96 #Gör bokstaven man lagt som val till siffra
            if row_number < 1 or row_number > boardsize  or row_number > int(boardsize) or column < 1 or column > int(boardsize):
                print("Coordinates were not within the given intervals.\n")
                continue
            if answer[row_number - 1][column - 1].isCompleted() == True:
                print("Du kan ej välja en bricka som e visad")
                continue
            if answer[row_number-1][column-1].isHidden() == False:
                print("du kan ej välja samma bricka du valt innan")
                continue
            else:
                if answer[row_number - 1][column - 1].isHidden() == True:
                    answer[row_number - 1][column - 1].setBoxIsNotHiddenAnymore()
                coordinatesOK = True
        except IndexError:
            print("Nej")
            continue
        if coordinatesOK:
            return row_number, column, answer

def show_choice(answer,boardshow,*tiles):
    tempShowBoard = copy.deepcopy(boardshow)
    print(tempShowBoard)
    print(answer)
    print(len(boardshow))
    for rows in range(len(boardshow)):
        for columns in range(len(boardshow[0])):
            if (rows, columns) in tiles:
                tempShowBoard[rows][columns] = answer[rows][columns]
                #print(tempShowBoard[rows][columns])
                Print_Board(tempShowBoard)

def checkIfWordIsChosen(boardshow, answer,rowIndex, columnIndex):
    gameOver = False

    if boardshow[rowIndex][columnIndex].isCompleted() == False and boardshow[rowIndex][columnIndex].isHidden() == True: #and boardshow[rowIndex2][columnIndex2].isCompleted() == False and boardshow[rowIndex2][columnIndex2].isHidden() == True:  # if the word is not selected
        if answer[rowIndex][columnIndex] == answer[rowIndex][columnIndex]:
            boardshow[rowIndex1][columnIndex1].setBoxIsCompleted() #and boardshow[rowIndex2][columnIndex2].setBoxIsCompleted()
            boardshow[rowIndex1][columnIndex1].setBoxIsNotHiddenAnymore() #and boardshow[rowIndex2][columnIndex2].setBoxIsNotHiddenAnymore()
        else:
            print("Box is already opened. Choose another option\n")


def main(): #main function
    vinst = False
    turn = 1
    boardsize, boardsizehalf = sizeOfGame()
    #BoardSelect = createSelectBoard(boardsize)
    answer = randomwords(boardsize, boardsizehalf)
    boardshow = createBoard(boardsize)
    gameOver = False
    #turnCoordstoIndex(BoardSelect, val1, boardsize, answer, boardshow)
    #show_choice(answer, boardshow, (RowIndex, ColIndex))
    while gameOver == False:
        Print_Board(answer)
        RowIndex1, ColIndex1, answer = getCoordinates(turn, boardsize, answer)
        Print_Board(answer)
        #show_choice(answer,boardshow,(RowIndex1-1, ColIndex1-1))
        RowIndex2, ColIndex2, answer = getCoordinates(turn, boardsize, answer)
        #show_choice(answer,boardshow,(RowIndex1-1, ColIndex1-1), (RowIndex2-1, ColIndex2-1))
        turn+=1

    #    printQuestions()
    #    action = input()
    #    actionOK = checkInputIsOK(action, 1, 2)
    #    if actionOK: #if the input from the user is either 1 or 2 then the program will enter the following if-statement
    #        gameOver = determineNextOperation(board, action, row-1, column-1)
main()