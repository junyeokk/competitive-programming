n = int(input())

r = False
l = False
u = False
d = False

max_x = -10 ** 9
min_x = 10 ** 9
max_y = -10 ** 9
min_y = 10 ** 9

for i in range(n):
    x, y, dr = map(str, input().split())
    x = int(x)
    y = int(y)
    if dr == 'R':
        r = True
        if x > max_x:
            max_x = x
    if dr == 'L':
        l = True
        if x < min_x:
            min_x = x
    if dr == 'U':
        u = True
        if y > max_y:
            max_y = y
    if dr == 'D':
        d = True
        if y < min_y:
            min_y = y

if r and l and u and d:
    print((min_x - max_x - 1) * (min_y - max_y - 1))
else:
    print("Infinity")