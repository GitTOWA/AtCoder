s = str(input())

ls = []

count = ""

for i in s:
    count += i
    if count == "dream" or count == "erase" or count == "dreamr" or count == "eraser":
        ls.append(count)
        count = ""

x = "".join(ls)

if x == s:
    print("YES")
else:
    print("NO")