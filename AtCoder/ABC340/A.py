A, B, C = map(int,input().split())

ans = []
total = A

while True:
  ans.append(total)
  if A == B:
    break
  total += C
  if total == B:
    ans.append(total)
    break


print(*ans)