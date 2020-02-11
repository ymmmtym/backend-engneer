# coding: utf-8

s = input().rstrip().split(' ')
n, m, c = int(s[0]),int(s[1]),int(s[2])

b = input().rstrip().split(' ')

a = []
count = 0
sum = c
for i in range(n):
    a = input().rstrip().split(' ')
    for j in range(m):
        sum += int(a[j])*int(b[j])
    a.clear()
    if sum > 0:
        count += 1
    sum = c

print(count)
