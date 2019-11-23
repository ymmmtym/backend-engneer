# coding: utf-8

s = input()

a1 = ['A','T']
a2 = ['C','G']

if s in a1:
    l = a1
else:
    l = a2

t = l.pop(l.index(s))
print(l[0])
