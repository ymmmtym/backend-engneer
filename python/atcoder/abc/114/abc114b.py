# coding: utf-8

s = input()
n = len(s)

l = [abs(753 - int(s[i]+s[i+1]+s[i+2])) for i in range(n-2)]
print(min(l))
