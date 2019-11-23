# coding: utf-8

a, b, k = map(int, input().split())

l = []
x = min(a,b)
for i in range(1,x+1):
    if a%i==0 and b%i==0:
        l.append(i)

print(l[-k])
