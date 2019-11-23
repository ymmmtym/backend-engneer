n = int(input())
p = list(map(int, input().split()))
count = 0

for i in range(n-2):
    list = [p[i],p[i+1],p[i+2]]
    if min(list) != p[i+1] and max(list) != p[i+1]:
        count += 1

print(count)
