kg = float(input("Hur mycket väger ditt paket? "))
if kg < 2 :
    print("Ditt paket kostar", 30 * kg , "kronor")
elif kg < 6 :
    print("Ditt paket kostar", 28 * kg , "kronor")
elif kg < 12:
    print("Ditt paket kostar", 25 * kg, "kronor")
else :
    print("Ditt paket kostar", 23 * kg , "kronor")

#kg är enkel att komma ihåg för kilogram, svårt att förknippa med annat
