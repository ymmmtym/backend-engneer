l = int(input())
n = int(input())
w = sorted(list(map(int,input().split())))
cnt = len(w)

while w and w[0] <= l:
    l -= w.pop(0)
print(cnt - len(w))