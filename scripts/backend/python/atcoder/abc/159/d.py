import collections

n = int(input())
a = list(map(int,input().split()))
d = collections.Counter(a)
s = sum([i*(i-1)//2 for i in d.values()])

for j in a:
    print(s-d[j]+1)