bingo_area = []
bingo_ch = []
bingo = False

for i in range(3):
  a = list(map(int,input().split()))
  bingo_area.append(a)

n = int(input())

for i in range(n):
  x = int(input())
  bingo_ch.append(x)

for i in range(3):
  for j in range(3):
    if bingo_area[i][j] in bingo_ch:
      bingo_area[i][j] = True
    else:
      bingo_area[i][j] = False

for i in range(3):
  if bingo_area[0][i] and bingo_area[1][i] and bingo_area[2][i]:
    bingo = True
  if bingo_area[i][0] and bingo_area[i][1] and bingo_area[i][2]:
    bingo = True

if bingo_area[0][0] and bingo_area[1][1] and bingo_area[2][2] or bingo_area[0][2] and bingo_area[1][1] and bingo_area[2][0]:
  bingo = True

print(bingo)
"""
84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30
"""