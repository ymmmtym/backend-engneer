# coding: utf-8

n = int(input())

count = 0
for i in range(n+1):
    s = str(i)
    l = sorted(list(set([j for j in s])))
    if l == ['3','5','7']:
        count+= 1

print(count)
