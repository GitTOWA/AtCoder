s = list(map(int,input().split()))

count = 0
app = []

# for i in range(9):
#     for j in range(9):
#         x = i + j
#         y = str(i) + str(j)
#         if y >= str(s[0]):
#             break
#         else:
#             if s[1] <= x <= s[2]:
#                 app.append(int(y))

for i in range(1,s[0]+1):
    ls = []
    for j in str(i):
        ls.append(int(j))
    x = sum(ls)
    if s[1] <= x <= s[2]:
        app.append(i)

print(sum(app))