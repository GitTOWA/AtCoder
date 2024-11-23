N = int(input())
S = input()

tura = 0
one = ""
two = ""
result = "No"
out = "Yes"
ans = []

for i in S:
  if i == "/":
    tura += 1
    continue
  if tura % 2 == 0:
    if i == "1":
      one += i
    else:
      out = "No"
      ot = one+two
      ans.append(ot)
      continue
  else:
    if i == "2":
      two += i
    else:
      out = "No"
      ot = one+two
      ans.append(ot)
      continue

print(ans)

if len(one) == len(two) and out == "Yes":
  result = "Yes"

print(result)
