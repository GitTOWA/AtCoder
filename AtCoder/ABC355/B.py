n, m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

result = "No"

total = a + b
total.sort()

a.sort()
alist = []

for i in range(len(a) - 1):
  alist.append([a[i],a[i+1]])
  

for i in range(len(total) - 1):
  lin = [total[i],total[i+1]]
  for i in alist:
    if lin == i:
      result = "Yes"

print(result)