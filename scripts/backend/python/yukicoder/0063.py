l,k = map(int,input().split())
d = -1 if l % (k*2) == 0 else 0
print((l//(k*2)+d)*k)