import random
import string
from memoryClassFile import Game
from memoryClassFile import Player

def PlayerName(): #Funktion som tar namnet av spelaren, med felhantering
    nameOK = False
    while nameOK == False:
        print("What is your name?")
        Playername = input()
        if Playername.isalpha():
            nameOK = True
        else:
            print("Name should only contain letters. \n")
    return Playername.capitalize() #Gör forsta bokstaven stort och resten små

def ReadHighscore():
    playerList = []
    try: #Försöker kolla om #this will try if the file 'top10List.txt' exist. If not, the function will continue into creating one.
        file = open("toptenhighscore.txt")
        playerListFromFile = file.read().split("\n")
        print(playerListFromFile)
        for i in range(1, len(playerListFromFile)):
            try: #if the file exists, the following lines will take out score from each line in the file if possible
                tempList = playerListFromFile[i].split()
                ScoreFromFile = int(tempList[1])
                playerList.append(Player(tempList[0], ScoreFromFile))
            except:
                pass
    except:
        pass
    return playerList

def PrintScoreBoard(playerList):
    print("\nTOP 10 LEADERBOARD:")
    for i in range(len(playerList)):
        print(playerList[i])

def AddPlayerToFile(playerList):
    file = open("toptenhighscore.txt", "w+")
    file.writelines("Leaderboard:\n")
    linesOfText = []
    for i in range(len(playerList)):
        score = playerList[i].Score()
        stringToAppend = f"{playerList[i].Name()} {score} poäng\n"
        linesOfText.append(stringToAppend)
    file.writelines(linesOfText)

def PrintScore(Score): #när spelet är slut visas poängen som spelaren fått
    print("Poäng:", Score)

def updateScoreBoardboard(Playername, Score): #Efter man vunnit uppdateras leaderboard, om mer än 10 pers har score tas den tionde platsen bort, funktionen visar dessutom leaderboarden
    playerList = ReadHighscore()
    playerList.append(Player(Playername, int(Score)))
    playerList.sort(key=lambda player: player.Score())
    if len(playerList) > 10:
        playerList.remove(playerList[10])
    PrintScoreBoard(playerList)
    AddPlayerToFile(playerList)

def sizeOfGame(): # Frågar spelaren om hur stor spelbrädan ska vara
    boardsizeOK = False
    minValue = 2 #minst 2, jämna tal oxå
    while boardsizeOK == False:
        print("Vad ska storleken på brädan vara? Storleken är AxA, välj endast A? (A: ")
        boardsize = input()
        boardsizeOK = checkInputOK(boardsize, minValue)
    boardsizehalf = int((int(boardsize)**2)/2)
    difficulty = int(input("Hur långa ord vill du spela med"))
    return int(boardsize), boardsizehalf, difficulty #Returnar rätt värde pga funktionen checkInputOK

def checkInputOK(value, minValue): #Funktion som kollar om banans storlek är korrek
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

def importrandomwords(): #Function som hämtar ord från txt fil och väljer random ord
    allwords = [] #tom lista där alla ord från hela memory3.txt filen läggs in
    infile = open("memory3.txt", "r")
    for line in infile:
        allwords.append(line.replace("\n", "")) #lägger in alla ord samt tar bort \n och byter ut mot ingenting, vilket gör att de går bort.
    infile.close() #stänger infilen
    return allwords

def makeboard (boardsizehalf, boardsize, allwords, difficulty):
    board_row=[]   #Listan med alla ord som ska delas upp till AxA
    for _ in range(boardsizehalf): #väljer antal rader beroende på hur stor spelbräda man har, tar ett random ord och lägger in det i rand_list, i boardsizehalf antal gånger
        randword = random.choice(allwords)
        board_row.append(Game(randword, difficulty))
        board_row.append(Game(randword, difficulty))
    random.shuffle(board_row) #blandar alla ord i board_row listan
    memoryboard = list(divide_boardlist(board_row, boardsize)) #anropar funktionen divide_boardlist så att den delar upp memoryboardlistan jämnt i AxA beroende på hur stort man valt att man vill spela.
    return memoryboard

def divide_boardlist(Alist, size): #funktion som slicar upp board_row listan till jämnt 6x6
    # loopar längden till listan
    for i in range(0, len(Alist), size):
        yield Alist[i:i + size] #yield används för att beräkna hela listan i lista, med return returnas endast första listan och ej lista i lista.

def Print_Board(memoryboard, difficulty): #printar boarden
    print("  ", end="")
    for i in range(1, len(memoryboard[0]) + 1):
        print("\t", i, end=" ")
        print('{0:>{1}d}'.format(i, difficulty+1), end="")
    print()
    for index, row in enumerate(memoryboard):
        print(string.ascii_uppercase[index], end="\t") #string.ascii_uppercase från import string för att displaya A, B, C, D... osv
        for word in row:
            print(word, end=" ")
        print()

def getIndex(turn, boardsize, memoryboard): #en funktion som frågar spelaren om vilket kort den ska välja och kollar om det går.
    CoordinatesOK = False
    print("val", turn, ":")
    while CoordinatesOK == False:
        choice = input("var vill du gå?").lower() #oavsett om man skriver litet a eller stort A blir input automatiskt litet A för att omvandla bokstaven till siffra
        try:
            row = choice[0] #sparar endast bokstaven från inputen i row, om man väljer A1 sparas A i row
            column = int(choice[1]) #sparar endast siffran från inputen om man väljer A1, sparas 1 i column och den omvandlas från string till integer
            for character in row:
                row_number = ord(character) - 96 #Gör bokstaven man lagt som val till siffra
            if row_number < 1 or row_number > boardsize or row_number > int(boardsize) or column < 1 or column > int(boardsize):
                print("Coordinates were not within the given intervals.\n")
                continue
            if memoryboard[row_number - 1][column - 1].isCompleted() == True and memoryboard[row_number-1][column-1].isHidden() == False:#om valet man valt har parats tidigare kan man ej välja den brickan igen
                print("Du kan ej välja en bricka som e visad")
                continue
            elif memoryboard[row_number-1][column-1].isHidden() == False: #om man valt A1 i första valet kan man ej välja A1 igen för att få samma ord
                print("du kan ej välja samma bricka du valt innan")
                continue
            else:
                coordinatesOK = True
        except IndexError:
            print("Du måste skriva något!")
            continue
        if coordinatesOK:
            return row_number-1, column-1

def ShowWord(memoryboard, row_number, column):
    memoryboard[row_number][column].setWordIsNotHiddenAnymore()  # ordet går från hidden till isnothidden.

def checkWordIsSame(memoryboard, RowIndex1, ColIndex1, RowIndex2, ColIndex2):
    if memoryboard[RowIndex1][ColIndex1] == memoryboard[RowIndex2][ColIndex2]:
        memoryboard[RowIndex1][ColIndex1].setWordIsCompleted()
        memoryboard[RowIndex2][ColIndex2].setWordIsCompleted()
        print("De var samma!")
    elif memoryboard[RowIndex1][ColIndex1] != memoryboard[RowIndex2][ColIndex2]:
        memoryboard[RowIndex1][ColIndex1].setWordIsHiddenAgain()
        memoryboard[RowIndex2][ColIndex2].setWordIsHiddenAgain()

def checkIfGameWon(memoryboard, boardsize):
    GameWon = False
    amountOfWords = boardsize**2
    amountOfCompletedWords = countCompletedWords(memoryboard,boardsize, "countCompletedWords")
    if amountOfCompletedWords == (amountOfWords):
        GameWon = True
        Print_Board(memoryboard)
        print("GRATTIS!! DU HITTA ALLA ORD!!")
    return GameWon

def countCompletedWords(memoryboard, boardsize, operation): #Function som räknar antal ord som är Completed för att kunna avsluta spelet om alla ord är öppnade.
    CompleteCount = 0
    if operation == "countCompletedWords":
        for row in range(boardsize):
            for column in range(boardsize):
                if memoryboard[row][column].isHidden() == False and memoryboard[row][column].isCompleted() == True:
                    CompleteCount += 1
    return CompleteCount



def main(): #main function
    turn = 1
    Playername = PlayerName()
    boardsize, boardsizehalf, difficulty = sizeOfGame()
    allwords = importrandomwords()
    memoryboard = makeboard(boardsizehalf, boardsize, allwords, difficulty)
    GameWon = False
    while GameWon == False:
        Print_Board(memoryboard, difficulty)
        RowIndex1, ColIndex1 = getIndex(turn, boardsize, memoryboard)
        ShowWord(memoryboard, RowIndex1, ColIndex1)
        Print_Board(memoryboard, difficulty)
        RowIndex2, ColIndex2 = getIndex(turn, boardsize, memoryboard)
        ShowWord(memoryboard, RowIndex2, ColIndex2)
        Print_Board(memoryboard, difficulty)
        checkWordIsSame(memoryboard, RowIndex1, ColIndex1, RowIndex2, ColIndex2)
        GameWon = checkIfGameWon(memoryboard, boardsize)
        if GameWon:
            PrintScore(turn)
            updateScoreBoardboard(Playername, turn)
        else:
            turn+=1


main()