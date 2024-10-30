s = input()

count = 0
ans = []

for i in s:
  if i == "|":
    count += 1
  if count == 1 or i == "|":
    pass
  else:
    ans.append(i)

result = "".join(ans)

print(result)