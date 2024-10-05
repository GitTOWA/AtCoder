s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))

total1 = 0
total2 = 0

for i in s1:
  total1 += i

for i in s2:
  total2 += i

if total1 >= total2:
  total = total1 - total2 + 1

print(total)