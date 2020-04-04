n = int(input())
digit_set = {0,1,2,3,4,5,6,7,8,9}

for i in range(n):
    a,b,c,d,r = map(str,input().split())
    if r == 'YES':
        digit_set &= set(list(map(int,[a,b,c,d])))
    else:
        digit_set -= set(list(map(int,[a,b,c,d])))

print(list(digit_set)[0])

