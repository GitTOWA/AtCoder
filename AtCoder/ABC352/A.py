s = list(map(int,input().split()))

num = sorted([s[1], s[2]])

if num[0] < s[3] < num[1]:
  print("Yes")
else:
  print("No")