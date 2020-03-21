import math


s,f = map(int,input().split())

if s % f == 0:
    ans = s//f+1
else:
    ans= math.ceil(s/f)

print(ans)