n = int(input())
l = ['']*n

for i in range(n):
    a,b = map(int, input().split())
    l[i] = max(a,b)

ans = sum(l)
print(ans)
