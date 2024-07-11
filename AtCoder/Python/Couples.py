"""
3
1 2 1 3 2 3
"""

s1 = int(input())
s2 = list(map(int,input().split()))

x = []
count = 0

for i in range(len(s2)):
    flag = True
    for j in range(3):
        if len(s2) == i + j:
            flag = False
        if flag == False:
            break
        x.append(s2[i + j])
        if len(x) == 3:
            if x[0] != x[1] and x[0] == x[2]:
                count += 1
            x = []
    if flag == False:
        break

print(count)