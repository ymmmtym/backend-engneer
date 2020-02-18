# coding: utf-8

def gcd_list(l):
    for i in range(len(l)-1):
        x = max(l[i],l[i+1])
        y = min(l[i],l[i+1])
        if x%y==0:
            return y
        else:
            while x%y!=0:
                z = x%y
                x = y
                y = z
            else:
                return z

n = int(input())
a = list(map(int, input().split()))

x = gcd_list(a)

print(x)
