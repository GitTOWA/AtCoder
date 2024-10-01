s1 = int(input())
s2 = list(map(int,input().split()))

count = 0

for i in s2:
  count += 1
  if len(s2[count:]) < 1:
    pass
  else:
    x = i * s2[count]
    print(x)