N = input()

num = []

for i in N:
  if i not in num:
    num.append(i)

for i in num:
  x = str(str(N).count(i))
  if x == i:
    result = "Yes"
  else:
    result = "No"
    break

print(result)