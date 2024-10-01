s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))

ans = []

for i in s2:
  if i % s1[1] == 0:
    x = round(i / s1[1])
    ans.append(x)

print(*ans)