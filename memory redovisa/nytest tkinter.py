import random
from memoryClassFileA import *
from tkinter import *



def firstWindow():
    """First window that take in-data such as the player's name, choices of width, height and amount of bombs."""
    global playerName, sizeChoice
    minSize = 2
    maxSize = 8
    playerName = StringVar()
    sizeChoice = StringVar()
    welcomeMessage = Label(root, text="Welcome to Memory!").grid(row=1, column=0, columnspan=2, sticky=N + E + S + W) #välkomsttext i mitten högst upp
    welcomeMessage2 = Label(root, text="Try to find all the matching cars logos!").grid(columnspan=2) #hsnabb beskrivning på vad man ska göra
    name = Label(root, text="Name:").grid(row=3, column=0)
    nameEntry = Entry(root, width=25, textvariable=playerName).grid(row=3, column=1) #box där man skriver sitt namn
    sizeLabel = Label(root, text="Choose size").grid(row=4, column=0)
    possibleSizeChoices = []
    for i in range(minSize, maxSize+1):
        if i % 2 == 0:
            possibleSizeChoices.append(i)
    sizeMenu = OptionMenu(root, sizeChoice, *possibleSizeChoices).grid(row=4, column=1, sticky=W)
    submitSizeButton = Button(root, text="Submit Size", command=submitSizeClick).grid(row=4, column=2, rowspan=2, columnspan=2, sticky = N+W+E+S)

def submitSizeClick():
    """When clicking the 'Submit Size' button."""
    global size, amountOfPictures, boardSizeHalf
    size = int(sizeChoice.get())
    amountOfPictures = (int(sizeChoice.get()))**2
    boardSizeHalf = int(amountOfPictures/2)
    playGame()  # initiates the game

def playGame():
    """Initiates the game"""
    main()
    global turn, allWords
    turn = 1
    gameIsOver = False
    boardWindow = Tk()
    boardWindow.title("Memory")

    getPictures(boardWindow)
    #createGraphBoard(boardWindow, gameWon)
    #printGrapBoard(gameOver)

def importRandomWords():  # Function som hämtar ord från txt fil och väljer random ord
    global allWords
    allWords = [] #tom lista där alla ord från hela memorywords.txt filen läggs in
    infile = open("memorywordsA.txt", "r")
    for line in infile:
        allWords.append(line.replace("\n", "")) #lägger in alla ord samt tar bort \n och byter ut mot ingenting, vilket gör att de går bort.
    print(allWords)
    infile.close() #stänger infilen

def makeBoard(boardSizeHalf, size, allWords):
    boardRow = []  # list with all the words in a single list, this list will be used to create a new sliced list
    for line in range(boardSizeHalf):  # choosing number of words that should be added in the game depending on how large of board the player has chosen
        randWord = random.choice(allWords)  # chooses a random word from allWords
        boardRow.append(Game(randWord))  # adds the word that is chosen in boardRow and in the object Game
        boardRow.append(Game(randWord))  # adds the same word in the list boardRow and in the object Game, this to give them different object ID's
    random.shuffle(boardRow)  # when all words have been added in the game, the words will be shuffled in a random orientation
    memoryBoard = list(divideBoardlist(boardRow, size))  # creates the memoryBoard function that is a sliced version of boardRow
    return memoryBoard

def divideBoardlist(listToSlice, sliceSize):  # this function slices the desired list to an even number of rows and elements
    for i in range(0, len(listToSlice), sliceSize):
        yield listToSlice[i:i + sliceSize]  # yield is used to give more than one return in the function, the function runs untill the size of the board is evenly sliced


def getPictures(boardWindow):
    """Function that gets all the pictures that are necessary for the program. Pictures have boardWindow as their master,
    hence the parameter."""
    global unopenedBoxPic, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eightteen, nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour, twentyfive, twentysix, twentyseven, twentyeight, twentynine, thirty, thirtyone, thirtytwo
    unopenedBoxPic = PhotoImage(master=boardWindow, file="minesweeperUnopenedSquare.png").subsample(35, 35)
    one = PhotoImage(master=boardWindow, file="one.png").subsample(5, 5)
    two = PhotoImage(master=boardWindow, file="two.png").subsample(5, 5)
    three = PhotoImage(master=boardWindow, file="three.png").subsample(5, 5)
    four = PhotoImage(master=boardWindow, file="four.png").subsample(5, 5)
    five = PhotoImage(master=boardWindow, file="five.png").subsample(5, 5)
    six = PhotoImage(master=boardWindow, file="six.png").subsample(5, 5)
    seven = PhotoImage(master=boardWindow, file="seven.png").subsample(5, 5)
    eight = PhotoImage(master=boardWindow, file="eight.png").subsample(5, 5)
    nine = PhotoImage(master=boardWindow, file="nine.png").subsample(5, 5)
    ten = PhotoImage(master=boardWindow, file="ten.png").subsample(5, 5)
    eleven = PhotoImage(master=boardWindow, file="eleven.png").subsample(5, 5)
    twelve = PhotoImage(master=boardWindow, file="twelve.png").subsample(5, 5)
    thirteen = PhotoImage(master=boardWindow, file="thirteen.png").subsample(5, 5)
    fourteen = PhotoImage(master=boardWindow, file="fourteen.png").subsample(5, 5)
    fifteen = PhotoImage(master=boardWindow, file="fifteen.png").subsample(5, 5)
    sixteen = PhotoImage(master=boardWindow, file="sixteen.png").subsample(5, 5)
    seventeen = PhotoImage(master=boardWindow, file="seventeen.png").subsample(5, 5)
    eightteen = PhotoImage(master=boardWindow, file="eightteen.png").subsample(5, 5)
    nineteen = PhotoImage(master=boardWindow, file="thirteen.png").subsample(5, 5)
    twenty = PhotoImage(master=boardWindow, file="twenty.png").subsample(5, 5)
    twentyone = PhotoImage(master=boardWindow, file="twentyone.png").subsample(5, 5)
    twentytwo = PhotoImage(master=boardWindow, file="twentytwo.png").subsample(5, 5)
    twentythree = PhotoImage(master=boardWindow, file="twentythree.png").subsample(5, 5)
    twentyfour = PhotoImage(master=boardWindow, file="twentyfour.png").subsample(5, 5)
    twentyfive = PhotoImage(master=boardWindow, file="twentyfive.png").subsample(5, 5)
    twentysix = PhotoImage(master=boardWindow, file="twentysix.png").subsample(5, 5)
    twentyseven = PhotoImage(master=boardWindow, file="twentyseven.png").subsample(5, 5)
    twentyeight = PhotoImage(master=boardWindow, file="twentyeight.png").subsample(5, 5)
    twentynine = PhotoImage(master=boardWindow, file="twentynine.png").subsample(5, 5)
    thirty = PhotoImage(master=boardWindow, file="thirty.png").subsample(5, 5)
    thirtyone = PhotoImage(master=boardWindow, file="thirtyone.png").subsample(5, 5)
    thirtytwo = PhotoImage(master=boardWindow, file="twentytwo.png").subsample(5, 5)

def createGraphicalBoard(boardWindow, gameOver):
    """Creates a list with lists as element containing button. They are put on the parameter boardWindow"""
    global graphicalMemoryBoard
    #preboard = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eightteen, nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour, twentyfive, twentysix, twentyseven, twentyeight, twentynine, thirty, thirtyone, thirtytwo]
    graphicalMemoryBoard = []
    for x in range(size):
        graphicalMemoryBoard.append([])
        for y in range(size):
            button = Button(boardWindow, image=unopenedBoxPic)
            button.bind("<Button-1>", lambda e, x=x, y=y: openBox(x, y, boardWindow, gameOver, gameIsWon))
            graphicalBoard[x].append(button)

def printGraphicalBoard(gameOver):
    """Prints the graphical board, which is a matrix with buttons"""
    if gameOver == False:
        for row in range(len(graphicalMemoryBoard)):
            for column in range(len(graphicalMemoryBoard[0])):
                graphicalMemoryBoard[row][column].grid(row=row, column=column)
    else:
        for row in range(len(graphicalMemoryBoard)):
            for column in range(len(graphicalMemoryBoard[0])):
                box = memoryBoard[row][column]
                if Game.isHidden() and box.isHidden():
                    graphicalMemoryBoard[row][column].config(image=bombPic)
                    graphicalMemoryBoard[row][column].grid(row=row, column=column)
                else:
                    graphicalMemoryBoard[row][column].grid(row=row, column=column)

def openBox(rowIndex1, columnIndex1, rowIndex2, columnIndex2):
    """Left click on a button"""
    box1 = memoryBoard[rowIndex1][columnIndex1]
    #button = graphicalMemoryBoard[rowIndex][columnIndex]
    if box1.isHidden() == True:
        box1.setWordIsNotHiddenAnymore()
        #configurePicture(amountOfContiguousBombs, button)
    box2 = memoryBoard[rowIndex2][columnIndex2]
    if box2.isHidden() == True:
        box2.setWordIsNotHiddenAnymore()
    if box1 == box2:
        box1.setWordIsCompleted()
        box2.setWordIsCompleted()
        print("Match! Good job!")
    elif box1 != box2:
        box1.setWordIsHiddenAgain()
        box2.setWordIsHiddenAgain()
        print("They did not match, try again!")

def checkIfGameWon(boardSize):  # function that checks whether the game has ben completed fully
    gameWon = False
    amountOfWords = boardSize ** 2
    amountOfCompletedWords = countCompletedWords(memoryBoard, boardSize, "countCompletedWords")
    if amountOfCompletedWords == amountOfWords:  # checks whether the amount of completed words is the ame number of amount of words that are in the game
        gameWon = True
        printBoard(memoryBoard, difficulty)
        print("CONGRATULATIONS! YOU FOUND ALL THE WORDS!!")
    return gameWon
def countCompletedWords(memoryBoard, boardSize, operation):  # function that counts the amount of compelted words to see wether the game is over or not.
    completeCount = 0
    if operation == "countCompletedWords":
        for row in range(boardSize):
            for column in range(boardSize):
                if memoryBoard[row][column].isHidden() == False and memoryBoard[row][column].isCompleted() == True:  # if word is both isHidden==False and isCompleted==True then the count goes up 1 word
                    completeCount += 1
    return completeCount
def main():
    importRandomWords()
    global memoryBoard
    memoryBoard = makeBoard(boardSizeHalf, size, allWords)

if gameOver == False:
    gameIsWon = checkIfGameWon(amountOfBombs)
    printGraphicalBoard(gameOver)
    ifGameHasFinished(boardWindow, gameOver, gameIsWon)


root = Tk()
root.title("Memory")
firstWindow()
root.mainloop()