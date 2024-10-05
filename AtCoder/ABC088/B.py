s1 = int(input())
s2 = list(map(int,input().split()))

s2.sort(reverse=True)

total = 0

for i in range(s1):
    if i % 2 == 0:
        total += s2[i]
    else:
        total -= s2[i]
print(total)