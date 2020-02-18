# coding: utf-8

y,m,d= map(int, input().split('/'))

x = 'TBD'
if y <= 2019:
    if m <= 4:
        x = 'Heisei'

print(x)
