n, k = map(int,input().split())
a = list(map(int,input().split()))

count = 0
ans = 0

while True:
  total = k
  # print("----------------")
  for i in range(count, n):
    total -= a[i]
    # print(k,total)
    if total >= 0:
      count += 1
    if total == 0 or total < 0:
      ans += 1
      break
  if count >= n:
    if total != 0:
      ans += 1
    break

print(ans)
