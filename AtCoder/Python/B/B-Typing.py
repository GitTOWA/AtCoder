"""
1つ目の文字列を用意する。
さっさんは1つ目の文字列通りに文字を入力しようとして何度かタイピングミスをしてしまった。
ミスした文字を残したまま最後まで入力を終えた。
1つ目と2つ目の文字列で何文字目が一致しているか求めよ。

入力例1
        abc
        asbvnc
    例2
        ganbattene
        ganbattene
実行結果1
        1 3 6
    結果2
        1 2 3 4 5 6 7 8 9 10
"""

s1 = str(input())
s2 = str(input())

x = []
count = 0

for i in s1:
    y = 0
    for j in s2:
        count += 1
        y += 1
        if i == j:
            x.append(count)
            s2 = s2[y:]
            break
print(*x)