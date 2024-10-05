a, b, c ,d = map(int,input().split())

le = a + b
ri = c + d

if le < ri:
  result = "Right"
elif le > ri:
  result = "Left"
else:
  result = "Balanced"

print(result)