s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))

count = 0
total = s1[1]
for i in range(len(s2)):
    total -= s2[i]
    if total < 0:
        break
    else:
        count += 1

print(count)