import collections

a = str(input())
b = str(input())

print('YES') if collections.Counter(a) == collections.Counter(b) else print('NO')