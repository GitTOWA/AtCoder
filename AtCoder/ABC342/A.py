x = input()

li = list(x)

for i in li:
  if li.count(i) > 1:
    result = i
    break

count = 0

for i in li:
  count += 1
  if result != i:
    break

print(count)
