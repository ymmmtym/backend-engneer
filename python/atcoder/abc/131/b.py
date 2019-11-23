n,l = map(int,input().split())

list = [l+i for i in range(n)]
sum = sum(list)

abs_list = [abs(l+i) for i in range(n)]
abs_min_taste_index = abs_list.index(min(abs_list))

ans = sum - list[abs_min_taste_index]
print(ans)
