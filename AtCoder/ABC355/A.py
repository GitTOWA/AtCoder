s1 = list(map(int,input().split()))
p = abs(s1[0] + s1[1])
m = abs(s1[0] - s1[1])
ans = [1,2,3]
if s1[0] == s1[1]:
  print(-1)
elif p in ans:
  print(p)
elif m in ans:
  print(m)