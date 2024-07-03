s1 = int(input())
s2 = list(map(int,input().split()))

count = 0
flag = True

while flag:
    i = 0
    for j in s2:
        if j % 2 != 0:
            flag = False
        elif j % 2 == 0:
            s2[i] = j / 2
        i += 1
    if flag:
        count += 1

print(count)