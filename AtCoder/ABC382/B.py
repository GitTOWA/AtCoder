N, D = input().split()

S = input()
count = 0
result = []
ans = ""

for j in S[::-1]:
  if j == "@" and count < int(D):
    count += 1
    result.append(".")
  else:
    result.append(j)

for i in result[::-1]:
  ans += i

print(ans)