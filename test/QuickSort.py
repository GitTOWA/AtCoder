s = list(map(int, input().split()))

if len(s) <= 1:
  sorted_s = s
else:
  pivot = s[len(s) // 2]
  left = []
  middle = []
  right = []

  for x in s:
    if x < pivot: #符号を反転させたら降順
      left.append(x)
    elif x == pivot:
      middle.append(x)
    else:
      right.append(x)

  sorted_s = left + middle + right

print(sorted_s)

"""
4 18 25 20 9 13
"""