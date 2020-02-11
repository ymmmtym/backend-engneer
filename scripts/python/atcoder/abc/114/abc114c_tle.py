# coding: utf-8

n = int(input())

count = 0
for i in range(n+1):
    s = str(i)
    if '1' not in s and '2' not in s and '3' in s and '4' not in s and '5' in s and '6' not in s and '7' in s and '8' not in s and '9' not in s:
        count += 1
print(count)
