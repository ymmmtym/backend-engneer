n,k = map(int,input().split())
s = str(input())

cnt = 1
if s[k-1] == '(':
    while True:
        if s[k] == '(':
            cnt += 1
        else:
            cnt -=1
        if cnt == 0:
            print(k+1)
            break
        k += 1
else:
    while True:
        if s[k-2] == ')':
            cnt += 1
        else:
            cnt -=1
        if cnt == 0:
            print(k-1)
            break
        k -= 1
