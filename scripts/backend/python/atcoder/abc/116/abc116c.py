# coding: utf-8

n = int(input())
h = list(map(int, input().split()))

c = 0
d = 0

for i in range(n-1):
    if h[i] > h[i+1]:
        c += h[i]
        d = h[i+1]
        if i == n - 2:
            c -= d
    elif i == n - 2:
        c += h[i+1] - d

print(c)
