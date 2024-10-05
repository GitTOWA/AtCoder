x, y = map(int, input().split())

ans = (x + y) / 2

if ans != int(ans):
    ans = int(ans) + 1
else:
    ans = int(ans)

print(ans)

# import math

# x, y = map(int, input().split())

# ans = (x + y) / 2

# print(math.ceil(ans))