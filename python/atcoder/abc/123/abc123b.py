# coding: utf-8

l = [int(input()) for i in range(5)]

sum = 0
div = 10

for i in l:
    if i % 10 != 0:
        sum += i + 10 - (i % 10)
        if i % 10 < div:
            div = i % 10
    else:
        sum += i

if div != 10:
    sum += div - 10

print(sum)
