# coding: utf-8

n = int(input())
l = []

for i in range(n):
    start,end = map(str, input().split('-'))
    if int(start[3])<5:
        start_about = int(start[:3]+'0')
    else:
        start_about = int(start[:3]+'5')
    if int(end[3])==0:
        end_about = int(end[:3]+'0')
    elif int(end[3])<=5:
        end_about = int(end[:3]+'5')
    else:
        if int(end[2])<5:
            end_about = int(end[:3]+'0')+10
        else:
            end_about = int('{0:02d}'.format(int(end[:2])+1)+'00')
    l.append(['{0:04d}'.format(start_about),'{0:04d}'.format(end_about)])

if n == 1:
    print('{0:04d}'.format(int(start_about))+'-'+'{0:04d}'.format(int(end_about)))
else:
    l.sort(key=lambda l: l[0])
    start_tmp,end_tmp = l[0][0],l[0][1]
    for i in range(n-1):
        start_next,end_next = l[i+1][0],l[i+1][1]
        if end_tmp < start_next:
            print('{0:04d}'.format(int(start_tmp))+'-'+'{0:04d}'.format(int(end_tmp)))
            if i < n-2:
                start_tmp,end_tmp = start_next,end_next
            else:
                print('{0:04d}'.format(int(start_next))+'-'+'{0:04d}'.format(int(end_next)))
        elif end_tmp < end_next:
            if i < n-2:
                end_tmp = end_next
            else:
                print('{0:04d}'.format(int(start_tmp))+'-'+'{0:04d}'.format(int(end_next)))
        else:
            if i == n-2:
                print('{0:04d}'.format(int(start_tmp))+'-'+'{0:04d}'.format(int(end_tmp)))
