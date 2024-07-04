# s1 = int(input())

# ls = []
# flag = True

# for i in range(s1):
#     s,ss,sss = map(int,input().split())
#     ls.append([s,ss,sss])
#     ls.append(map(int,input().split()))

# if len(ls) == 2:
#     if ls[0][1] == ls[1][1] and ls[0][2] == ls[1][2]:
#         result = "No"
#     else:
#         ans = abs(ls[0][0] - ls[1][0])
#         for i in range(ans):
#             x1 = ls[0][1] + i
#             x2 = ls[0][1] - i
#             for j in range(ans):
#                 y1 = ls[0][2] + j
#                 y2 = ls[0][2] - j
#                 if ls[1][1] == x1 and ls[1][2] == y1 or ls[1][1] == x2 and ls[1][2] == y2:
#                     result = "Yes"
#                     flag = False
#                     break
#                 else:
#                     result = "No"
#             if flag == False:
#                 break
# else:
#     if 0 == ls[0][1] and 0 == ls[0][2]:
#         result = "No"
#     else:
#         ans = abs(0 - ls[0][0])
#         for i in range(ans):
#             x1 = 0 + i
#             x2 = 0 - i
#             for j in range(ans):
#                 y1 = 0 + j
#                 y2 = 0 - j
#                 if ls[0][1] == x1 and ls[0][2] == y1 or ls[0][1] == x2 and ls[0][2] == y2:
#                     result = "Yes"
#                     flag = False
#                 else:
#                     result = "No"
#             if flag == False:
#                 break
            
# print(result)


