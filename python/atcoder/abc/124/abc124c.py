# coding: utf-8

s = input()
n = len(s)
m = n // 2

if n%2 == 0:
    x = '01'*m
    y = '10'*m
else:
    x = '01'*m + '0'
    y = '10'*m + '1'

l = [0,0]
for i in range(n):
    if s[i] != x[i]:
        l[0] += 1
    if s[i] != y[i]:
        l[1] += 1

print(min(l))
