n = int(input())
t,a = map(int, input().split())
h = list(map(int, input().split()))

d = []

for i in range(n):
    temp = t - (h[i] * 0.006)
    d.append(abs(a - temp))

ans = d.index(min(d))+1
print(ans)
