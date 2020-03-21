n = int(input())
a = sorted(list(map(int,input().split())))
if n%2 == 1:
    ans = a[(n+1)//2-1]
else:
    ans = round((a[n//2-1]+a[n//2])/2,1)
print(ans)