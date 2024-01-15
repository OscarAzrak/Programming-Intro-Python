import TVprog
filnamn = "simulering.txt"

try:
    with open(filnamn, 'r') as file:  # read a list of lines into data
        data = file.readlines()
        vardagsTV = TVprog.TV( data[0].rstrip(), data[1].rstrip(), int(data[2].rstrip()))
        koksTV = TVprog.TV( data[0 + 4].rstrip(),data[1 + 4].rstrip(), int(data[2 + 4].rstrip()))
except IOError:
    print('Something went wrong...')
print(vardagsTV)
print(koksTV)