# coding: utf-8

S = input().rstrip().split(' ')
s = input().rstrip().split(' ')

C = int(S[0])
c = int(s[0])
R = int(S[1])
r = int(s[1])

a = C*R - r*C - R*c +r*c

print(a)
