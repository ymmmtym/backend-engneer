r,D,x = map(int, input().split())

def nextWeight(n):
    if n == 0:
        return x
    else:
        return r*nextWeight(n-1)-D

for i in range(1,11):
    print(nextWeight(i))
