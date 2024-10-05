x, y, z = map(int,input().split())

ans = x * y

lists = [ans, z]

box = lists[0]

for i in lists:
  if i <= box:
    box = i

print(box)