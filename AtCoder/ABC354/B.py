n = int(input())

user = []
total = 0

for i in range(n):
  s = input().split()
  user.append(s)

for i in range(n):
  total += int(user[i][1])

ans = total - (int((total / n)) * n)

user.sort()

print(user[ans][0])