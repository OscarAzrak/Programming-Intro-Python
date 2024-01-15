import random
def start():
    tarning = []
    Kast = 1
    Tar = 1
    Tstr = ""
    Tantal = int(input("Hur många tärningar behövs i spelet? "))
    Kantal = int(input("Hur många kast en spelare får?"))
    for i in range(0, Tantal):
        T = random.randint(1, 6)
        tarning.append(T)
        print("Tärning {}: ".format(Tar), tarning[-1])
        Tar += 1
    Tar = 1
    while Kast < Kantal:
        svar = input("Vill du kasta igen? Svara med j/n ")
        if svar == "j":
            tarning.clear()
            for i in range(0, Tantal):
                T = random.randint(1, 6)
                tarning.append(T)
                print("Tärning {}: ".format(Tar), tarning[-1])
                Tar += 1
            Tar = 1
            Kast = Kast + 1
        elif svar == "n":
            for i in tarning:
                Tstr += str(i) + ", "
            print("Du fick: {}".format(Tstr[:-2]), ".")
            break
    if Kast == Kantal:
        for i in tarning:
            Tstr += str(i) + ", "
        print("Du fick: {}".format(Tstr[:-2]), ".")


while True:
    svar1 = input("Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A: ")
    if svar1 == "":
        start()
        continue
    elif svar1 == "A":
        break

