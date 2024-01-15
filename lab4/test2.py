import numpy as np

rad = int(input("hur många rader? "))
col = int(input("hur många kollumner ska spelet vara? "))
board = []
row = 11
col = col + 10
for i in range(rad):
    row_list = []
    for j in range(row, col + 1):
        row_list.append(j)
    board.append(row_list)
    row = row + 10
    col = col + 10
board[0][0] = str("P ")
for row in board:
    for elem in row:
        print(elem, end=" ")
    print()
h = int(input("vadda"))
p = board.index(h)
while p <= rad:
    del board[p][-1]
    p += 1

for row in board:
    for elem in row:
        print(elem, end=" ")
    print()