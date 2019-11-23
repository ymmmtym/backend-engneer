n, m = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse=True)

if n>=m or m == 1:
    S =0
else:
    d = sorted([l[i] - l[i+1]  for i in range(m-1)], reverse=True)
    S = max(l) - min(l)
    for i in range(n-1):
        S -= d[i]

print(S)
