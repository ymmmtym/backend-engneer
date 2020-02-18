# coding: utf-8

n, m = map(int, input().split())
stores = sorted([tuple(map(int,input().split())) for _ in range(n)])

price = 0
count = 0

for j in range(n):
    if count == m:
        break
    for k in range(int(stores[j][1])):
        if count < m:
            price += int(stores[j][0])
            count += 1
        else:
            break

print(price)
