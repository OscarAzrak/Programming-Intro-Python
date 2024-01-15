rad = int(input("Hur många rader? "))
board = []
row = 11
col = int(input("Hur många kolumner? "))
col = col + 10
for i in range(rad):
    row_list = []
    for j in range(row, col + 1):
        row_list.append(j)
    board.append(row_list)
    row = row + 10
    col = col + 10
board[0][0] = "P "
for row in board:
    for elem in row:
        print(elem, end=" ")
    print()
#    hittatal(board,v)
v = int(input("Välj ditt tal? "))
h = 0



def indexx(x, y):
    for l in board:
        for i in l:
            if i == v:
                x = l.index(i)
                y = board.index(l)
    return x, y
indrad = 0
indcol = 0
a, b = indexx(indrad, indcol)

print(b)
print(a)

while b < rad:
    del board[b][a:]
    b += 1
print(board)

for row in board:
    for elem in row:
        print(elem, end=" ")
    print()