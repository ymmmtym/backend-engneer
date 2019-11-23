# coding: utf-8

m = input().rstrip().split(' ')
deg = int(m[0])/10   # 風向
dis = int(m[1])/60   # 風力

if deg >= 11.25 and deg < 33.75:
    dir = 'NNE'
elif deg >= 33.75 and deg < 56.25:
    dir = 'NE'
elif deg >= 56.25 and deg < 78.75:
    dir = 'ENE'
elif deg >= 78.75 and deg < 101.25:
    dir = 'E'
elif deg >= 101.25 and deg < 123.75:
    dir = 'ESE'
elif deg >= 123.75 and deg < 146.25:
    dir = 'SE'
elif deg >= 146.25 and deg < 168.75:
    dir = 'SSE'
elif deg >= 168.75 and deg < 191.25:
    dir = 'S'
elif deg >= 191.25 and deg < 213.75:
    dir = 'SSW'
elif deg >= 213.75 and deg < 236.25:
    dir = 'SW'
elif deg >= 236.25 and deg < 258.75:
    dir = 'WSW'
elif deg >= 258.75 and deg < 281.25:
    dir = 'W'
elif deg >= 281.25 and deg < 303.75:
    dir = 'WNW'
elif deg >= 303.75 and deg < 326.25:
    dir = 'NW'
elif deg >= 326.25 and deg < 348.75:
    dir = 'NNW'
else:
    dir = 'N'


if dis >= 0 and dis < 0.25:
    dir = 'C'
    w = 0
elif dis >= 0.25 and dis < 1.55:
    w = 1
elif dis >= 1.55 and dis < 3.35:
    w = 2
elif dis >= 3.35 and dis < 5.45:
    w = 3
elif dis >= 5.45 and dis < 7.95:
    w = 4
elif dis >= 7.95 and dis < 10.75:
    w = 5
elif dis >= 10.75 and dis < 13.85:
    w = 6
elif dis >= 13.85 and dis < 17.15:
    w = 7
elif dis >= 17.15 and dis < 20.75:
    w = 8
elif dis >= 20.75 and dis < 24.45:
    w = 9
elif dis >= 24.45 and dis < 28.45:
    w = 10
elif dis >= 28.45 and dis < 32.65:
    w = 11
else:
    w = 12

print(dir + ' ' + str(w))
