# coding: utf-8

n, q = map(int, input().split())
s = input()

ac = []
for i in range(n-1):
    if s[i:i+2] == 'AC':
        ac.append(i+1)

count = len(ac)
for i in range(q):
    l,r = (map(int, input().split()))
    x = sum(j<l for j in ac)
    y = sum(j>r for j in ac)
    count = count - x - y
    print(count)
