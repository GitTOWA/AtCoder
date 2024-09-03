s1 = list(map(int,input().split()))

num = []

for i in range(s1[0]):
    num.append(i+1)

li = sorted(num[s1[1]-1:s1[2]])

num[s1[1]-1:s1[2]] = li[::-1]
print(*num)