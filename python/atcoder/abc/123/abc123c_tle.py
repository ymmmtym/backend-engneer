# coding: utf-8

n = int(input())
l = [int(input()) for i in range(5)]

a = [n,0,0,0,0,0]
m = len(a)

count = 0

while a[m-1] < n:
    for j in range(len(l)):
        i = len(l) - j - 1
        if a[i+1] == n:
            break
        if a[i] != 0:
            if a[i] > l[i]:
                a[i] -= l[i]
                a[i+1] += l[i]
            else:
                a[i+1] += a[i]
                a[i] = 0
    count += 1

print(count)
