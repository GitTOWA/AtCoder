n = int(input())
a = int(input())

while True:
  if n >= 500:
    n -= 500
  else:
    break

ans = n - a

if ans <= 0:
  print("Yes")
else:
  print("No")