N, Q = input().split()

T = list(map(int, input().split()))

Tm = []
x = int(N)
total = 0

for i in T:
  if i not in Tm:
    Tm.append(i)
    x -= 1
  else:
    Tm.remove(i)
    x += 1

print(x)