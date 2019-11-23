# coding: utf-8

x,y,z,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

a.reverse()
b.reverse()
c.reverse()

l = []

for i in a:
    for j in b:
        for m in c:
            l.append(i+j+m)

l.sort()
l.reverse()

for i in range(k):
    print(l[i])
