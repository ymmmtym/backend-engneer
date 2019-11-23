# coding: utf-8

n,k = map(int, input().split())
s = input()

low = s[k-1].lower()
print(s[:k-1]+low+s[k:])
