import random
import string
import re
from memoryClassFileC import Game
from memoryClassFileC import Player
def printIntro():
    print("Hello and welcome to Memory! Try to find all the wordpairs!")
    print("Play by choosing a entering a letter and then a number, for example : A1")
    print("The game will count how many times you have tried opening a pair and that will be your score")
    print("Have fun and enjoy!")
    print("Best regards,")
    print("Oscar, creator of Memory!\n")

def playerName(): #Function that asks for player's name and controlling if its only letter in the name
    nameOK = False
    while nameOK == False:
        print("What is your name?")
        nameOfPlayer = input()
        if nameOfPlayer.isalpha(): #Checks if the player's name only contains alphabetic letters, letters such äs åäö also works
            nameOK = True
        else:
            print("Name should only contain letters. \n")
    return nameOfPlayer.capitalize() #returns the name of player with the  first letter in name as capital (if input = memory, return is Memory)

def readHighscore(): #function that saves the players name from the Highscorefile to a list that contains all information from file
    playerList = [] #list that will contain all playernames with their respective scores
    try: #this will try to open the file 'toptenhighscore.txt' if it exists. If it does not exist, the function will create the file.
        file = open("toptenhighscore.txt")
        playerListFromFile = file.read().split("\n")
        for i in range(1, len(playerListFromFile)):
            try:# if the file exists, the score and name will be stored and added to playerList
                tempList = playerListFromFile[i].split() #a temporary list that will copy each line from the textfile to a new list
                scoreFromFile = int(tempList[1]) #scoreFromFile is a variable with each score from each line
                playerList.append(Player(tempList[0], scoreFromFile)) #adds in playerList list the name and score for each player in to the class Player
            except:
                pass
    except:
        pass
    return playerList

def printScoreBoard(playerList): #displays the top 10 best scores at the end of a game
    print("\nTOP 10 LEADERBOARD:")
    for i in range(len(playerList)):
        print(playerList[i]) #prints the player and their score line for line from the playerList list

def addPlayerToFile(playerList): #function that add the players and scores in the text file
    file = open("toptenhighscore.txt", "w+")
    file.writelines("Leaderboard:\n")
    linesOfText = []
    for i in range(len(playerList)):
        score = playerList[i].Score()
        stringToAppend = f"{playerList[i].Name()} {score} Poäng\n"
        linesOfText.append(stringToAppend)
    file.writelines(linesOfText)

def printScore(score):#When game is over, the player's score is displayed
    print("Poäng:", score)

def updateScoreBoardboard(playerName, score): #After the game is over, the leaderboard is updated, if more than 10 player has entered the highscore, the last player on the number 10 spot will be deleted.
    playerList = readHighscore()
    playerList.append(Player(playerName, int(score)))
    playerList.sort(key=lambda player: player.Score())
    if len(playerList) > 10:
        playerList.remove(playerList[10])
    printScoreBoard(playerList)
    addPlayerToFile(playerList)

def sizeOfGame(): #function that asks player what size the player want their board to be, function also checks if the size is okay.
    boardSizeOK = False
    minSize = 2
    maxSize = 10
    while boardSizeOK == False:
        print("What width and length do you want your board to be? Width and length has to be same size, answer with only one number: ")
        boardSize = input() #Saves player's input for size in boardSize
        boardSizeOK = checkInputOK(boardSize, minSize, maxSize) #runs function to see if the sizd is okay, otherwise the game will ask for a new input.
    boardSizeHalf = int((int(boardSize)**2)/2) #a variable of how many unique words should be added in the game, this will be used later.
    return int(boardSize), boardSizeHalf  # returns a correct value of boardSize because of the function checkInputOK.

def checkInputOK(size, minSize, maxSize): #function that checks wether the size of the board is correct
    okInput = False
    try:
        size = int(size)
        if size >= minSize and size <= maxSize and size%2 == 0:# answer has to be larger than 2 and be dividable with two, an even number
            okInput = True
        else:
            print("Size should be in between", minSize,"and", maxSize,"and the size has to be an even number.")
    except ValueError:
        print("Wrong input. Type in an integer.")
    return okInput

def importrandomwords(): #Function som hämtar ord från txt fil och väljer random ord
    allWords = [] #empty list where all words from textfile memorywords will be added, word for word.
    infile = open("memorywords.txt", "r")
    for line in infile:
        allWords.append(line.replace("\n", ""))#adds all words in allWords and removes the \n from the list
    infile.close() #stänger infilen
    return allWords

def makeBoard (boardSizeHalf, boardSize, allWords):
    boardRow=[]  #list with all the words in a single list, this list will be used to create a new sliced list
    for line in range(boardSizeHalf): #choosing number of words that should be added in the game depending on how large of board the player has chosen
        randWord = random.choice(allWords) #chooses a random word from allWords
        boardRow.append(Game(randWord)) #adds the word that is chosen in boardRow and in the object Game
        boardRow.append(Game(randWord)) #adds the same word in the list boardRow and in the object Game, this to give them different object ID's
    random.shuffle(boardRow) #when all words have been added in the game, the words will be shuffled in a random orientation
    memoryBoard = list(divideBoardlist(boardRow, boardSize)) #creates the memoryBoard function that is a sliced version of boardRow
    return memoryBoard

def divideBoardlist(listToSlice, sliceSize): #this function slices the desired list to an even number of rows and elements
    for i in range(0, len(listToSlice), sliceSize):
        yield listToSlice[i:i + sliceSize] #yield is used to give more than one return in the function, the function runs untill the size of the board is evenly sliced

def printBoard(memoryBoard): #This function prints the board
    print("  ", end="")
    for i in range(1, len(memoryBoard[0]) + 1):
        print("\t", i, end=" ")
    print()
    for index, row in enumerate(memoryBoard):
        print(string.ascii_uppercase[index], end="\t")#the module string is imported to be able to convert a number to a number, this makes it easy to display A, B, C ....
        for word in row:
            print(word, end=" ")
        print()

def getChoice(turn, boardSize, memoryBoard): #a function that asks the player what word they want to open and also checks wether their input is correct
    coordinatesOK = False
    print("val", turn, ":")
    while coordinatesOK == False:
        choice = input("What card do you wish to open?, write your letter first and then your number with no space between \n").lower() #if the players writes in capitals or non-capital letters the input will be transformed to lowercase letters so the function can easly transform letter to a number to get indices
        choice = re.split("(\d+)", choice) #function that seperates letters from numbers from input
        for emptyelement in choice:
            if emptyelement == "":
                choice.remove(emptyelement)
        if len(choice) != 2:
            print("Wrong input, try again! Write one letter and one number that is within the board's range. Example format: A1")
            continue
        if boardSize < 10:
            if len(choice[0]) !=1:
                print("Wrong input, try again! Write only one letter that is within the board's range. Example format: A1")
                continue
            if len(choice[1]) !=1:
                print("Wrong input, try again! Write only one number that is within the board's range. Example format: A1")
                continue
        else:
            if len(choice[0]) !=1:
                print("Wrong input, try again! Write only one letter that is within the board's range. Example format: A1")
                continue
            if int(choice[1]) > 10:
                print("Wrong input, try again! Write only one integer that is within the board's range. Example format: A10")
                continue

        try:
            row = choice[0] #stores only the letter from input in row, if choice = A1, only lowercase a is saved
            column = int(choice[1]) # stores only the number from input in column, if choice = A1, only 1 is saved, and is stored as an integer
            for character in row:
                rowNumber = ord(character) - 96  #converts the letter in row to a number, this is why lowercase is cruical, lowercase letter 'a' had a number 1 and 'b' is number 2, and so on.
            if rowNumber < 1 or rowNumber > boardSize or rowNumber > int(boardSize) or column < 1 or column > int(boardSize):
                print("Choice is outside the gameboard.")
                continue
            if memoryBoard[rowNumber - 1][column - 1].isCompleted() == True and memoryBoard[rowNumber-1][column-1].isHidden() == False: #if the word the player has chosen is both shown and completed, this means the player has chosen the right pair previosuly and will not be able to choose that spot again.
                print("You can't choose a shown card!")
                continue
            elif memoryBoard[rowNumber-1][column-1].isHidden() == False:# if a player chooses a word in the first choice, the player won't be able to choose that same choice again in the second inout.
                print("You can't choose the same card you've already chosen")
                continue
            else:
                coordinatesOK = True
        except ValueError:
            print("valueerror")
            continue
        except IndexError:
            print("indexerror")
            continue
        if coordinatesOK:
            return rowNumber-1, column-1

def showWord(memoryBoard, rowNumber, column):
    memoryBoard[rowNumber][column].setWordIsNotHiddenAnymore() #the word that is chosen goes from hidden to shown

def checkWordIsSame(memoryBoard, rowIndex1, colIndex1, rowIndex2, colIndex2):
    if memoryBoard[rowIndex1][colIndex1] == memoryBoard[rowIndex2][colIndex2]:
        memoryBoard[rowIndex1][colIndex1].setWordIsCompleted()
        memoryBoard[rowIndex2][colIndex2].setWordIsCompleted()
        print("Match! Good job!")
    elif memoryBoard[rowIndex1][colIndex1] != memoryBoard[rowIndex2][colIndex2]:
        memoryBoard[rowIndex1][colIndex1].setWordIsHiddenAgain()
        memoryBoard[rowIndex2][colIndex2].setWordIsHiddenAgain()
        print("They did not match, try again!")

def checkIfGameWon(memoryBoard, boardSize): #function that checks wether the game has ben completed fully
    gameWon = False
    amountOfWords = boardSize**2
    amountOfCompletedWords = countCompletedWords(memoryBoard,boardSize, "countCompletedWords")
    if amountOfCompletedWords == amountOfWords: #checks wether the amount of completed words is the ame number of amount of words that are in the game
        gameWon = True
        printBoard(memoryBoard)
        print("CONGRATULATIONS! YOU FOUND ALL THE WORDS!!")
    return gameWon

def countCompletedWords(memoryBoard, boardSize, operation): #function that counts the amount of compelted words to see wether the game is over or not.
    completeCount = 0
    if operation == "countCompletedWords":
        for row in range(boardSize):
            for column in range(boardSize):
                if memoryBoard[row][column].isHidden() == False and memoryBoard[row][column].isCompleted() == True: #if word is both isHidden==False and isCompleted==True then the count goes up 1 word
                    completeCount += 1
    return completeCount

def playAgain():
    playOK = True
    print("Do you want to play again? if yes type 'yes', otherwise press any key") #player can answer in both english or swedish
    playAgain = input().lower()
    while playOK:
        try:
            if playAgain[0] == "y" or playAgain[0] == "j": #checks wether the first letter in the input is 'y' or 'j'
                main() #the main function will run if the player chooses to play again
                playOK = False
            else:
                break
        except IndexError:
            break
def main(): #main function
    printIntro()
    turn = 1
    nameOfPlayer = playerName()
    boardSize, boardSizeHalf = sizeOfGame()
    allWords = importrandomwords()
    memoryBoard = makeBoard(boardSizeHalf, boardSize, allWords)
    gameWon = False
    while gameWon == False:
        printBoard(memoryBoard)
        rowIndex1, colIndex1 = getChoice(turn, boardSize, memoryBoard)
        showWord(memoryBoard, rowIndex1, colIndex1)
        printBoard(memoryBoard)
        rowIndex2, colIndex2 = getChoice(turn, boardSize, memoryBoard)
        showWord(memoryBoard, rowIndex2, colIndex2)
        printBoard(memoryBoard)
        checkWordIsSame(memoryBoard, rowIndex1, colIndex1, rowIndex2, colIndex2)
        gameWon = checkIfGameWon(memoryBoard, boardSize)
        if gameWon:
            printScore(turn)
            updateScoreBoardboard(nameOfPlayer, turn)
            playAgain()
        else:
            turn+=1


main()