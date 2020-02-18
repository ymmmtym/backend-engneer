# coding: utf-8

a, b = map(int, input().split())

x = 0

if a > b:
    x = 2*a -1
elif a < b:
    x = 2*b -1
else:
    x = 2*a

print(x)
