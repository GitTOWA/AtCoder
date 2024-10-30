import random

x,y = map(int,input().split())

num = [0,1,2,3,4,5,6,7,8,9]

xy = x+y

num.remove(xy)

answer = random.choice(num)

print(answer)