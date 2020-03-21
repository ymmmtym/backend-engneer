cnt = 0
for month in range(1,13):
    if month == 2:
        end = 28
    elif month in [4,6,9,11]:
        end = 30
    else:
        end = 31
    for day in range(1,end+1):
        if month == sum([int(i) for i in str(day)]):
            cnt += 1

print(cnt)