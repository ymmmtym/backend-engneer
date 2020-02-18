n = int(input())
l = ['']*n

for i in range(n):
    a,b = map(int, input().split())
    l[i] = a+b

ans = max(l)
print(ans)
