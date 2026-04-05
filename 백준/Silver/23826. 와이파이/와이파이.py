n = int(input())

rooms = []
flag = False
res = -1

for i in range(n + 1):
    x, y, e = map(int, input().split())
    rooms.append((x, y, e))

x0, y0, e0 = rooms[0]

for i in range(1, n + 1):
    xi, yi, ei = rooms[i]

    dst = abs(xi - x0) + abs(yi - y0)
    pub = max(0, e0 - dst)

    shot = 0
    for j in range(1, n + 1):
        xj, yj, ej = rooms[j]
        d = abs(xi - xj) + abs(yi - yj)
        shot += max(0, ej - d)

    s = pub - shot
    if s > 0:
        flag = True
        res = max(res, s)

if flag:
    print(res)
else:
    print("IMPOSSIBLE")