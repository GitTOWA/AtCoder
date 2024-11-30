N, D = input().split()

S = input()

count = S.count("@")

total = int(N) - count

result = int(D) + total

print(result)