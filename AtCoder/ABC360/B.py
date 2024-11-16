# s, t = map(str, input().split())

# ans = "No"

# for k in range(1, len(s) + 1):
#   result = ""
#   for j in range(k - 1, len(s), k):
#     result += s[j]
#   if result == t:
#     ans = "Yes"
#     break
#   if len(result) <= 1:
#     break


# print(ans)

S, T = input().split()
anslist = []
for i in range(1,len(S)):
    for j in range(i):
        ans = ""
        for k in range(j,len(S),i):
            ans += S[k]
        anslist.append(ans)
if T in anslist:
    print("Yes")
else:
    print("No")