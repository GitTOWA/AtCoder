s = int(input())

li = []

for i in range(s):
  x = int(input())
  li.append(x)
li.sort()
x = set(li)
print(len(x))
