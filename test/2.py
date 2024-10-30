# s = input()
# list = [[s[0], 0]]
# for i in s:
#   count = 0
#   for j in s:
#     if i == j:
#       count += 1
#   if list[0][1] < count:
#     list = [[i, count]]
#   elif list[0][1] == count and [i, count] not in list:
#     list.append([i, count])

# for i in range(len(list)):
#   print(list[i][0])


s = input()
char_count = {}

# 文字の出現回数を数える
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 最大の出現回数を取得
max_count = max(char_count.values())

# 最も出現回数の多い文字を全て出力
for char, count in char_count.items():
    if count == max_count:
        print(char)
