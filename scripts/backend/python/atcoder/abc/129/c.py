N,M = map(int,input().split())

tmp = 0
for i in range(M):
    broken = int(input())
    if tmp != 0 and broken - tmp == 1:
        print(0)
        break
    
