s = list(map(int, input().split()))

def create_sort(mode):
  for i in range(len(s)):
    for j in range(len(s) - 1):
      if mode == "asc":
        if s[j] > s[j + 1]:
          s[j], s[j + 1] = s[j + 1], s[j]
      else:
        if s[j] < s[j + 1]:
          s[j], s[j + 1] = s[j + 1], s[j]
  return s

print(create_sort("desc"))

"""
4 18 25 20 9 13
"""