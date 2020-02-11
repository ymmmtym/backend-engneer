N,M = map(int, input().split())
A = sorted(list(map(int, input().split())))

for i in range(M):
    B,C = map(int, input().split())
    A = sorted(A)
    for i in range(B):
        if C > A[i]:
            A[i] = C
        else:
            break

ans = sum(A)
print(ans)
