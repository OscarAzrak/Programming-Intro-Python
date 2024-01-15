import random
from memoryClassFileA import *
from tkinter import *


root = Tk()
def firstWindow():
    """First window that take in-data such as the player's name, choices of width, height and amount of bombs."""
    global playerName, sizeChoice
    minSize = 2
    maxSize = 10
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
    global turn
    turn = 1
    gameWon = False
    boardWindow = Tk()
    boardWindow.title("Memory")
    openPictures(boardWindow)
    createGraphBoard(boardWindow, gameWon)
    #printGrapBoard(gameOver)


def openPictures(boardWindow):
    """Function that gets all the pictures that are necessary for the program. Pictures have boardWindow as their master,
    hence the parameter."""
    global unopenedBoxPic, emptySquarePic, bombPic, openedBombPic, wronglyMarkedBomb, flagPic, one, two, three, four, five, six

    #unopenedBoxPic = PhotoImage(master=boardWindow, file="minesweeperUnopenedSquare.png").subsample(35, 35)
    #emptySquarePic = PhotoImage(master=boardWindow, file="minesweeperEmptySquare.png").subsample(3, 3)
    #bombPic = PhotoImage(master=boardWindow, file="minesweeperBomb.png").subsample(3, 3)
    #openedBombPic = PhotoImage(master=boardWindow, file="redbomb.png").subsample(15, 15)
    #wronglyMarkedBomb = PhotoImage(master=boardWindow, file="wrongBomb.png").subsample(5, 5)
    #flagPic = PhotoImage(master=boardWindow, file="Minesweeper_flag.png").subsample(45, 45)
    #one = PhotoImage(master=boardWindow, file="one.png").subsample(5, 5)
    #two = PhotoImage(master=boardWindow, file="two.png").subsample(5, 5)
    #three = PhotoImage(master=boardWindow, file="three.png").subsample(5, 5)
    #four = PhotoImage(master=boardWindow, file="four.png").subsample(5, 5)
    #five = PhotoImage(master=boardWindow, file="five.png").subsample(5, 5)
    #six = PhotoImage(master=boardWindow, file="six.png").subsample(4, 4)
def createGraphBoard(boardWindow, gameWon):
    """Creates a list with lists as element containing button. They are put on the parameter boardWindow"""
    global graphicalBoard
    graphicalBoard = []
    for x in range(size):
        graphicalBoard.append([])
        for y in range(size):
            button = Button(boardWindow, image=unopenedBoxPic)
            button.bind("<Button-1>", lambda e, x=x, y=y: openFirstBox(x, y, boardWindow, gameWon))
            #button.bind('<Button-3>', lambda e, x=x, y=y: flagBox(x, y, boardWindow, gameOver))


def openFirstBox(rowIndex, columnIndex, boardWindow, gameWon):
    """Left click on a button"""
    pic = memoryBoard[rowIndex][columnIndex]
    button = graphicalBoard[rowIndex][columnIndex]
    if pic.isHidden() == True:
        pic.setPicIsNotHiddenAnymore()

   # if gameOver == False:
   #     gameIsWon = checkIfGameIsWon(amountOfBombs)
   # printGraphicalBoard(gameOver)
   # ifGameHasFinished(boardWindow, gameOver, gameIsWon)


def makeBoard(boardSizeHalf, boardSize, allWords):
    global memoryBoard
    boardRow = []  # list with all the words in a single list, this list will be used to create a new sliced list
    for line in range(boardSizeHalf):  # choosing number of words that should be added in the game depending on how large of board the player has chosendef main():
        randPic = random.choice(allWords)  # chooses a random word from allWords
        boardRow.append(Game(randPic))  # adds the word that is chosen in boardRow and in the object Game    global memoryBoard
        boardRow.append(Game(randPic))  # adds the same word in the list boardRow and in the object Game, this to give them different object ID's    memoryBoard = makeBoard(boardSizeHalf, boardSize, allWords, difficulty)
    random.shuffle(boardRow)  # when all words have been added in the game, the words will be shuffled in a random orientation
    memoryBoard = list(divideBoardlist(boardRow, boardSize))  # creates the memoryBoard function that is a sliced version of boardRow

def divideBoardlist(listToSlice, sliceSize):  # this function slices the desired list to an even number of rows and elements
    for i in range(0, len(listToSlice), sliceSize):
        yield listToSlice[#    turn = 1
              i:i + sliceSize]  # yield is used to give more than one return in the function, the function runs untill the size of the board is evenly sliced#    nameOfPlayer = playerName()

def importRandomPics():  # Function som hämtar ord från txt fil och väljer random ord
    allPics = []  # empty list where all words from textfile memorywords will be added, word for word.


    infile = open("memorywordsB.txt", "r")
    for line in infile:
        wordsToAppend = line.strip()
        #allWords.append(wordsToAppend)
    infile.close()  # closes infile
    return #allWords


def main():

    global memoryBoard
    #allWords = importrandomwords()
    memoryBoard = makeBoard(boardSizeHalf, size, #allWords)

#    boardSize, boardSizeHalf, difficulty = sizeOfGameAndDifficulty()
#    allWords = importrandomwords(difficulty)
#    memoryBoard = makeBoard(boardSizeHalf, boardSize, allWords, difficulty)
#    gameWon = False
#    while gameWon == False:
#        printBoard(memoryBoard, difficulty)
#        rowIndex1, colIndex1 = getChoice(turn, boardSize, memoryBoard)
#        showWord(memoryBoard, rowIndex1, colIndex1)
#        printBoard(memoryBoard, difficulty)
#        rowIndex2, colIndex2 = getChoice(turn, boardSize, memoryBoard)
#        showWord(memoryBoard, rowIndex2, colIndex2)
#        printBoard(memoryBoard, difficulty)
#        checkWordIsSame(memoryBoard, rowIndex1, colIndex1, rowIndex2, colIndex2)
#        gameWon = checkIfGameWon(memoryBoard, boardSize, difficulty)
#        if gameWon:
#            printScore(turn)
#            updateScoreBoardboard(nameOfPlayer, turn)
#            playAgain()
#        else:
#            turn += 1


root=Tk()
#root.title("Bombsweeper")
#welcomingWindow()
root.mainloop()