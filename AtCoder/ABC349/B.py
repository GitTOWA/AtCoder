S = input()

Ss = []
num = []
nums = []
result = "Yes"

for i in S:
  if i not in Ss:
    Ss.append(i)

for i in Ss:
  count = S.count(i)
  num.append(count)

for i in num:
  if i not in nums:
    nums.append(i)

for i in nums:
  total = num.count(i)
  if total == 1:
    result = "No"
    break

print(result)