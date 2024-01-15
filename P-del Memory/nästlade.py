import string

boardshow = []  # tomlista där  - - -  osv läggs in beroende på hur stor bräda man vill ha
for i in range(6):
    row_list = []
    for j in range(1, 6 + 1):
        row_list.append("-----") #just nu är det 3 streck, ändra till variabel som beror på hur långa ord man vill ha.
    boardshow.append(row_list)
#om 3 streck, första innan alla siffror är 3, och den i for satsen är 3 och den vid ascii är 1
#om 5 streck försata innan alla andra är 5 och den i satsen är 5 och den vid ascii är 2
diffspace = 3
difficulty = 5
if difficulty == 5:
    diffspace = difficulty - 3
elif difficulty == 3:
    diffspace = difficulty-2

b = ('{0:^{1}}'.format(3, 4))


print(" "*(difficulty), end="")
for i in range(1, 7):
    print(b, end=" ")
print()
for index, row in enumerate(boardshow):
    print(string.ascii_uppercase[index], end=" "*(diffspace)) #string.ascii_uppercase från import string för att displaya A, B, C, D... osv
    for word in row:
        print(word, end=" ")
    print()
Word = "hej"
Difficulty = 8
print("då", end="")
x = 5

a = '{1:.{0}}'.format(x, 1.12345111)
print(a)
#for a in BoardSelect:
#    if val1 in a:
#        CoordinatesOK = True
#if CoordinatesOK:
#    print("Värdet finns inte spelplanen")
#else:
#    return CoordinatesOK