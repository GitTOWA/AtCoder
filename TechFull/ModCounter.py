s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))

ls = {}
for i in s2:
    x = i % s1[1]
    if x in ls:
        ls[x] += 1
    else:
        ls[x] = 1

c = 0
ans = 0
for i in ls:
    if c < ls[i]:
        c = ls[i]
        ans = i
print(ans)