n = int(input())
m = int(input())

for i in range(m):
    p,q = map(int,input().split())
    if n in [p,q]:
        n = p if n == q else q

print(n)
