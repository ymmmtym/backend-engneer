# coding: utf-8

n = int(input())

sum = 0
for i in range(n):
    x,u = map(str, input().split())
    x = float(x)
    if u == 'JPY':
        sum += x
    elif u == 'BTC':
        sum += x * 380000.0

print(sum)
