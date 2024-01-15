rad = int(input("Ange antal rader: "))
kol = int(input("Ange antal kollumner: "))

i = 1
print("", end="\t")
while i < kol + 1:
    print(i, end="\t")
    i += 1
print("\n")
k = 1
while k < rad + 1:
    for mult1 in range(1, rad + 1):
        print(mult1, end=" ")
        for mult2 in range(1, kol + 1):
            print("{:3d}".format(mult1 * mult2), end=" ")
        print("\n")
        k += 1
