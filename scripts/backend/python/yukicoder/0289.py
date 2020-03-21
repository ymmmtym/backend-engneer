import re


s = str(input())

num_str = re.sub("\\D", "", s)
ans = sum([int(i) for i in num_str])
print(ans)