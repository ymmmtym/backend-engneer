# coding: utf-8
import re

n,k = map(int, input().split())
s = input()

p1 = r"^0+1+(0+1+){k-1}"
p2 = r"1+(0+1+){k}"
p3 = r"(1+0+){k-1}1+0+$"
p4 = r"(1+0+){k}1+"

pattern = [p1,p2,p3,p4]
match = [re.findall(d,s) for d in pattern]

for i in match:
    if

print(match)
