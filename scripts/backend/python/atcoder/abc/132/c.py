n = int(input())
d = list(map(int,input().split()))

sorted_d = sorted(d)
half = n//2

a = sorted_d[half-1]
b = sorted_d[half]

print(b-a)
