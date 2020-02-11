s = input()

list_sorted = sorted([s[i] for i in range(4)])
if list_sorted[0] == list_sorted[1] and  list_sorted[2] == list_sorted[3] and list_sorted[1] != list_sorted[2]:
    print("Yes")
else:
    print("No")
