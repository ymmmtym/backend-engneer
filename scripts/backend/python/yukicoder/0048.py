import math


x = int(input())
y = int(input())
l = int(input())

if x == 0 and y >= 0:
    cnt = 0
elif y < 0:
    cnt = 2
else:
    cnt = 1

print(math.ceil(abs(x)/l)+math.ceil(abs(y)/l)+cnt)
