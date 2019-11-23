# coding: utf-8

s = input()
prefix = int(s[:2])
suffix = int(s[2:])

def isMonth(n):
    if n <= 12 and n >= 1:
        return True

if isMonth(prefix) and isMonth(suffix):
    ans = 'AMBIGUOUS'
elif not isMonth(prefix) and isMonth(suffix):
    ans = 'YYMM'
elif isMonth(prefix) and not isMonth(suffix):
    ans = 'MMYY'
else:
    ans = 'NA'

print(ans)
