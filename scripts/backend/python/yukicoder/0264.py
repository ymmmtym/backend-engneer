n,k = map(int, input().split())
d = n-k
if d == 0:
    result = 'Drew'
elif d == 1 or d == -2:
    result = 'Lost'
else:
    result = 'Won'
print(result)