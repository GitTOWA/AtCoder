S = input()

x = []

result = "No"

if len(S) % 2 == 0:
  for i in range(0, len(S), 2):
    if S[i] == S[i+1]:
      x.append(S[i])
    else:
      print(result)
      exit()
  for i in x:
    if S.count(i) == 2:
      result = "Yes"
    else:
      result = "No"
      break

print(result)