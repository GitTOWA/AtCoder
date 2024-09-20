s = int(input())
x = 1
count = 0
while True:
  x *= 2
  count += 1

  if x - 1 == s:
    count += 1
    break
  elif x > s:
    break


print(count)