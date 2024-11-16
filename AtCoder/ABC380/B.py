S = input()

haif = 0
haifList = []

for i in S:
  if i == "|":
    if haif != 0:
      haifList.append(haif)
    haif = 0
  if i == "-":
    haif += 1

print(*haifList)