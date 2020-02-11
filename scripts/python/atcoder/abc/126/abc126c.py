# coding: utf-8

n,k = map(int, input().split())

p = 0
for i in range(n):
    j = i + 1
    t = 0
    while j < k:
        j *= 2
        t += 1
    p += ((1/2)**t)/n

print(p)
