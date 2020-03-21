coins = [int(input()) for _ in range(3)]
l = [25,4,10]

for i in range(len(l)):
    if i != len(l)-1:
        coins[1-i] += coins[2-i]//l[i]
    coins[2-i] %= l[i]
print(sum(coins))
