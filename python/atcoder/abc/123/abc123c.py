# coding: utf-8
import math

n = int(input())
l = [int(input()) for i in range(5)]
l.sort()

a = math.ceil(n/l[0])+4
print(a)
