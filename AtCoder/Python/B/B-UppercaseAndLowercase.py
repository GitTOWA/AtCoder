s = str(input())

low = 0
up = 0

for i in s:
  if i == i.lower():
    low += 1
  else:
    up += 1

if low < up:
  result = s.upper()
else:
  result = s.lower()

print(result)