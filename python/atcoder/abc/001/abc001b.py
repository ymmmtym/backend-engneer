# coding: utf-8
m = int(input())
vv = 0

if m < 100:
    vv = 0
if m <= 5000:
    vv = m // 100
    if m < 1000:
        vv = "0" + str(vv)
if m >= 6000 and m <= 30000:
        vv = m//1000 + 50
if m >= 35000 and m <= 70000:
        vv = ((m//1000 - 30)//5)+80
if m > 70000:
        vv = 89

print(vv)
