s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())

count = 0
total = 0

# l1 = []
# l2 = []
# l3 = []

# for i in range(s1):
#     l1.append("500")

# for i in range(s1):
#     l2.append("100")

# for i in range(s1):
#     l3.append("50")


# for i in l1:
#     for j in l2:
#         for k in l3:
#             print(f"{i} + {j} + {k}")
#             total = i + j + k
#             if s4 == total:
#                 count += 1

for i in range(s1+1):
    for j in range(s2+1):
        for k in range(s3+1):
            # print(f"{500} * {i} + {100} * {j} + {50} * {k}")
            total = 500 * i + 100 * j + 50 * k
            if s4 == total:
                count += 1
print(count)