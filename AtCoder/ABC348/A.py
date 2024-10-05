s = int(input())

for i in range(1,s+1):
  if i % 3 == 0:
    print("x",end="")
  else:
    print("o",end="")