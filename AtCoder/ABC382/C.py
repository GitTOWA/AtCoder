N, M = input().split()

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(len(B)):
  none = True
  for j in range(len(A)):
    if B[i] >= A[j]:
      print(j+1)
      none = False
      break
  if none:
    print("-1")