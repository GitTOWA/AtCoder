# x = list(map(int,input().split()))

# count = 0

# for i in range(len(x)):
#   for j in range(i,len(x)):
#     if x[i] == x[j]:
#       x.remove(i)
#       count += 1

# print(count)

A = list(map(int,input().split()))

list = []
count = 0

for i in range(len(A)):
  if A[i] not in list:
    list.append(A[i])
    if A.count(A[i]) > 1:
      count += 1

print(count)
