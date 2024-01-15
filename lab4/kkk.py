def splan(height, width):

    Plan = [[(str(b) + str(h)) for h in range(1, height + 1)] for b in range(1, width + 1)]
    Plan[0][0] = str("P ")

    return Plan

def tabort(plan, dplan):

    for a in plan:
        for b in reversed(a):
            for c in dplan:
                if b in c:
                    a.remove(b)

    return plan

def spelplan(plan):

    for rad in plan:
        print(" ".join(map(str, rad)))

def gameover(plan):

    if sum(len(x) for x in plan) == 1:
        nVinst = True
    else:
        nVinst = False

    return nVinst

def inmatning(plan, turn):

    igen = True

    if (turn % 2) == 1:
        print("Spelare 1: ")
    else:
        print("Spelare 2: ")

    while igen:
        try:
            postion = str(input("Vart vill du gå? "))
            y = int(postion[0])
            x = int(postion[1])
        except ValueError:
            print("Du måste ange ett siffer värde")
            continue
        except IndexError:
            print("Det där du försöker göra uppskattas inte :( " )
            continue

        for a in plan:
            if postion in a:
                igen = False
        if igen:
            print("Värdet är inte tillåtet")

    dplan = [[(str(b) + str(h)) for h in range(x, height + 1)] for b in range(y, width + 1)]

    return dplan

def main():
    turn = 1
    nVinst = False
    Plan = splan(width, height)

    while not nVinst:

        spelplan(Plan)
        dplan = inmatning(Plan, turn)
        Plan = tabort(Plan, dplan)
        nVinst = gameover(Plan)

        turn += 1

    print("\n" + "GAME OVER")
    if (turn % 2) == 1:
        print("\n" + "Spelare 2 vinner!! ")
    else:
        print("\n" + "Spelare 1 vinner!!  ")

while True:
    try:
        width = int(input("Höjd? "))
        height = int(input("Bredd? "))
    except ValueError:
        print("Skriv in ett siffer värde")
        continue
    except IndexError:
        print("DÖ")
        continue

    if height > 9 or height < 2:
        print("Planen får inte vara så stor eller liten!! ")
        continue
    if width > 9 or width < 2:
        print("Planen får inte vara så stor eller liten!! ")
        continue
    else:
        break

main()
