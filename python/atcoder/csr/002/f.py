n = int(input())
l = ['']*n

for i in range(n):
    a,b = map(int, input().split())
    l[i] = (min(a,b),max(a,b))

ans = len(set(l))
print(ans)
