# coding: utf-8

n = int(input())

i = 1
while n > 0:
    if n == 4:
        break
    i += 1
    if n % 2 == 0:
        n = n / 2
    else:
        n = n*3+1

print(i+3)
