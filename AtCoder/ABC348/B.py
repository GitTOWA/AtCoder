N = int(input())

X = []
Anses = []
result = []

for i in range(N):
  x = list(map(int, input().split()))
  X.append(x)

for i in range(N):
  Ans = []
  for j in range(N):
    ans = ((X[i][0] - X[j][0])**2 + (X[i][1] - X[j][1])**2) ** 0.5
    Ans.append(ans)
  Anses.append(Ans)


for i in Anses:
  ts = 0
  ps = 0
  for count,j in enumerate(i):
    if j > ts:
      ts = j
      ps = count+1
  result.append(ps)

for i in result:
  print(i)