class Game: #Skapar class "Game" för att kolla när spelet tar slut
    def __init__(self, Word):
        self.__Word = Word
        self.__isCompleted = False
        self.__isHidden = True

    def __str__(self):
        stringtoshow = ""
        #for i in range(int(self.__Difficulty)):  VISA TOM BILD ISTÄLLET FÖR STRECK
        #    stringtoshow += "-"
        if self.__isHidden == True:
            return f"{stringtoshow}"
        else:
            return f"{self.__Word}"
    def __eq__(self, other):
        return self.__Word == other.__Word
    def __ne__(self, other):
        return self.__Word != other.__Word

    def isHidden(self):
        return self.__isHidden
    def isCompleted(self):
        return self.__isCompleted
    def setWordIsNotHiddenAnymore(self):
        self.__isHidden = False
    def setWordIsCompleted(self):
        self.__isCompleted = True
    def setWordIsHiddenAgain(self):
        self.__isHidden = True

class Player(): #klass för att spara top 10 spelare med lägst poäng i spelet
    def __init__(self, Name, Score):
        self.__Name = Name #Intans variabel för namnet av spelaren
        self.__Score = Score #Instansvariabel för hur många poäng spelaren fick

    def __str__(self):
        return f"{self.__Name}    Poäng: {self.__Score}"

    def Name(self):
        return self.__Name

    def Score(self):
        return self.__Score