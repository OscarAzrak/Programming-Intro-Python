import TVprog

filnamn = "simulering.txt"

try:
    with open(filnamn, 'r') as file:  # read a list of lines into data
        data = file.readlines()
        vardagsTV = TVprog.TV(data[1].rstrip(), int((data[2].rstrip())))
        koksTV = TVprog.TV(data[0 + 4].rstrip(), int(data[0 + 6].rstrip()))

except IOError:
    print('Something went wrong...')

def main():
    global tv, enhet
    while True:
        try:
            val = int(input('''
    *** Welcome to TV-simulator! Here we use two TV devices ***

    1. Vardagsrums TV
    2. Köks TV
    3. Avsluta
    Your choice: '''))

            if (val == 1):
                enhet = 0
                tv = vardagsTV
                tvMeny()

            elif (val == 2):
                enhet = 1
                tv = koksTV
                tvMeny()

            elif (val == 3):
                break
                file.close()
                quit()

            else:
                # Error control numbers
                print('Choose a number between 1 and 3')

        except BaseException as err:
            # Error control letters
            print('Choose a number between 1 and 3')


def tvMeny():
    # Displays second menu
    while True:
        try:
            print(tv)
            menyVal = int(input('''
1. Byt kanal
2. Sänk volymen 
3. Höj volymen
4. Tillbaka till huvudmenyn
Ditt val: '''))
            if (menyVal == 1):
                bytKanal()
            elif (menyVal == 2):
                tv.sankVolym()

                data[2 + 5 * enhet] = tv.volym + '\n'
                with open("simulering.txt", "w") as file:
                    file.writelines(data)
            elif menyVal == 3:
                tv.hojVolym()
                data[2 + 5 * enhet] = tv.volym + '\n'
                with open("simulering.txt", "w") as file:
                    file.writelines(data)

            elif (menyVal == 4):
                break
            else:
                # Error control "numbers"
                print('Choose a number between 1 and 4')
        except BaseException as err:
            # Error control "letters"
            print('Choose a number between 1 and 4')


def bytKanal():
    # Change channel and program
    while True:
        try:
            kanalVal = int(input('''Your choice: '''))
        except ValueError:
            print("Skriv med siffror")
            continue
        except IndexError:
            print("Nej")
            continue
        if kanalVal > 99 or kanalVal < 1:
            continue
        else:
            data[1 + 5 * enhet] = str(kanal) + '\n'
                # Error control numbers
                #print('Choose a number between 1 and 4')
            with open('simulering.txt', 'w') as file:
                file.writelines(data)
            tv.bytKanal()
            break
main()