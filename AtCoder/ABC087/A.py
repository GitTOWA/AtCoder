x = int(input())
a = int(input())
b = int(input())

ans = x - a

while True:
  ans -= b
  if ans < b:
    break

print(ans)