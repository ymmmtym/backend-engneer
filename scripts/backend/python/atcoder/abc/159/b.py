s = str(input())
n = len(s)
r = ''.join(list(reversed(s)))

print('Yes') if s == r and s[:(n-1)//2] == s[((n+3)//2)-1:] else print('No')