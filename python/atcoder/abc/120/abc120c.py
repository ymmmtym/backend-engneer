# coding: utf-8

s = input()
n = len(s)

a = s.count('0')
b = s.count('1')

x = min(a,b)*2
print(x)
