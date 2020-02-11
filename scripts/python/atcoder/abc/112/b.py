N,T = map(int, input().split())

c_list = []

for i in range(N):
    c,t = map(int, input().split())
    if t <= T: c_list.append(c)

print(min(c_list)) if len(c_list) > 0 else print('TLE')
