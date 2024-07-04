s = str(input())

ls = []

for i in s:
    if i == "R":
        ls.append(i)
    elif i == "M":
        ls.append(i)

if ls[0] == "R":
    print("Yes")
else:
    print("No")