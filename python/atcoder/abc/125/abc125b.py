# coding: utf-8

n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

x = 0

for i in range(n):
    if v[i] > c[i]:
        d = v[i] - c[i]
        x += d
print(x)
