s = str(input())


def woosaw(n,x):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = alphabet.find(x)
    return alphabet[(index-n)%len(alphabet)]
    

ans = ''
for i in range(len(s)):
    ans += woosaw(i+1,s[i])

print(ans)