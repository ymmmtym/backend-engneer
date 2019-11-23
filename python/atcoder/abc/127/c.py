N,M = map(int, input().split())
L = ['']*M
R = ['']*M

for i in range(M):
    L[i],R[i] = map(int, input().split())

id_l,id_r = max(L),min(R)
width = id_r - id_l + 1 if max(L)<=min(R) else 0

print(width)
