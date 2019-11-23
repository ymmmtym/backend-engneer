s = str(input())

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        ans = 'Bad'
        break
    else:
        ans = 'Good'

print(ans)
