# s = list(map(int,input().split()))

# li = []
# lj = []
# lk = []

# for i in range(s[0]+1):
#     for j in range(s[0]+1):
#         for k in range(s[0]+1):
#             x = 10000 * i + 5000 * j + 1000 * k
#             y = i + j + k
#             if x == s[1] and y == s[0]:
#                 li.append(i)
#                 lj.append(j)
#                 lk.append(k)

# if len(li):
#     print(li[0],lj[0],lk[0])
# else:
#     print(f"-1 -1 -1")

s = list(map(int, input().split()))

found = False

for i in range(s[0] + 1):
    for j in range(s[0] + 1 - i):
        k = s[0] - i - j
        if 10000 * i + 5000 * j + 1000 * k == s[1]:
            found = True
            break
    if found:
        break

if found:
    print(i, j, k)
else:
    print("-1 -1 -1")
