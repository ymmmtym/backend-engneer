n = int(input())
l = list(map(int, input().split()))

M = max(l)
S = sum(l)

if M*2<S :
    s = 'Yes'
else:
    s = 'No'

print(s)
