N = int(input())
A = []
B = []

for i in range(N*2):
  word = list(input())
  if i < N:
    A.append(word)
  else:
    B.append(word)
  
for i in range(len(A)):
  for j in range(len(A[i])):
    if A[i][j] != B[i][j]:
      result = i+1,j+1

print(*result)