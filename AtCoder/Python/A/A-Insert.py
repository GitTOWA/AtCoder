s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))

count = 0
add = []

for i in s2:
  add.append(i)
  count += 1
  if count  == s1[1]:
    add.append(s1[2])

print(*add)
