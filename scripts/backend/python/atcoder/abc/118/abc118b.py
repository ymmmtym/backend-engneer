# coding: utf-8

n, m = map(int, input().split())
s = set(range(1,m+1))

for _ in range(n):
    l = list(map(int, input().split()))
    s = s & set(l[1:])

print(len(s))
