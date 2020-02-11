# coding: utf-8

n, q = map(int, input().split())
s = input()

t = [0]*(n+1)
for i in range(n):
    if s[i:i+2] == 'AC':
        t[i+1] = t[i] + 1
    else:
        t[i+1] = t[i]

for i in range(q):
    l,r = (map(int, input().split()))
    ans = t[r-1] - t[l-1]
    print(ans)
