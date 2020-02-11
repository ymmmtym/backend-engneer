N = int(input())
l = []

for i in range(N):
    store,rank = map(str, input().split())
    number = i+1
    l.append([store,int(rank),number])

sorted_list = sorted(l, key=lambda x:(x[0],-x[1]))
for i in range(N):
    print(sorted_list[i][2])
