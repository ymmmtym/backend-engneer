# coding: utf-8

n, q = map(int, input().split())
s = input()

# time live error
for i in range(q):
    f,e = (map(int, input().split()))
    st = s[f-1:e]
    # print(st.count('AC'))
    count = 0
    for j in range(len(st)-1):
        if st[j] == 'A' and st[j+1] == 'C':
            count += 1
    print(count)
