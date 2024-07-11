s1 = int(input())

x = []
for i in range(s1):
    s2 = str(input())
    x.append(s2)

ans = x.count("Takahashi")

print(ans)