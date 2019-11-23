# coding: utf-8

n = int(input())

p = [int(input()) for i in range(n)]
x = sum(p) - max(p)//2

print(x)
