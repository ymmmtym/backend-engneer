# coding: utf-8

a, b, c = map(int, input().split())
M = max(a,b,c)
x = a*b*c//(M*2)
print(x)
