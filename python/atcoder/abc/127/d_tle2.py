N,M = map(int, input().split())
A = sorted(list(map(int, input().split())))
card_sum = sum(A)
l = []

for i in range(M):
    B,C = map(int, input().split())
    l.append([C]*B)

numbers = sorted([flatten for inner in l for flatten in inner],reverse=True)

for i in range(len(numbers)):
    if A[i] < numbers[i]:
        card_sum += numbers[i] - A[i]
    else:
        break
print(card_sum)
