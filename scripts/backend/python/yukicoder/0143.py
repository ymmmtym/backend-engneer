k,n,f = map(int,input().split())
beans = k*n
for i in map(int,input().split()):
    beans -= i

print(beans) if beans >= 0 else print(-1)