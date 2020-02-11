# coding: utf-8

s = input()
t = ['A','T','C','G']

count = 0
length = 0

for i in s:
    if i in t:
        count += 1
    elif count > length:
        length = count
        count = 0

print(count) if count > length else print(length)
