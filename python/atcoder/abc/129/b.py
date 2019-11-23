N = int(input())
W = list(map(int,input().split()))

sum_W = sum(W)
half_W = sum_W // 2
l_sum = 0
r_sum = sum_W

for i in range(N):
    if l_sum >= r_sum or i == N-1:
        ans_1 = l_sum - r_sum
        ans_2 = r_sum + W[i-1]*2 - l_sum
        print(min(ans_1,ans_2))
        break
    else:
        l_sum += W[i]
        r_sum -= W[i]
