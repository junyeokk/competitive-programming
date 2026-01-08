a, b = map(int, input().split())

res = [[0 for _ in range(b + 1)] for _ in range(b + 1)]

for _ in range(a):
    x, y = map(int, input().split())
    res[x][y] = 1
    res[y][x] = 1

for i in range(b):
    for j in range(b):
        print(res[i + 1][j + 1], end = ' ')
    print()
    