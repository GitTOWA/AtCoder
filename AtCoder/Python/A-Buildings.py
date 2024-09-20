s = int(input())
s1 = list(map(int,input().split()))

count = 0
for i in s1:
  count += 1
  if s1[0] < i:
    break

if count == s:
  count = -1
if s == 0:
  count = -1

print(count)