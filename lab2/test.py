pk = int(input("Hur många paket vill du skicka? "))
pknmr = 1
listaPaketOchVikt = {}
while pknmr <= pk :
    kg = int(input("Ange vikt för paket {} ".format(pknmr)))
    pknmr += 1
    if kg < 2 :
        kostnad = kg * 30
        listaPaketOchVikt['Paket', pknmr] = kostnad
    elif kg < 6 :
        kostnad = kg * 28
        listaPaketOchVikt['Paket', pknmr] = kostnad
    elif kg < 12:
        kostnad = kg * 25
        listaPaketOchVikt['Paket', pknmr] = kostnad
    else :
        kostnad = kg * 23
        listaPaketOchVikt['Paket', pknmr] = kostnad

print("Det kommer kosta" , sum(listaPaketOchVikt.values()) , "kronor.")

