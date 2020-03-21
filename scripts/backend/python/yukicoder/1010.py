x, y, h = map(int, input().split())

a = min(x,y)
b = max(x,y)
h = h/1000
count = 0

while True:
    if a > h:
        a /= 2
        h *= 2
        count += 1
    elif b > h:
        b /= 2
        h *= 2
        count += 1
    else:
        break

print(count)