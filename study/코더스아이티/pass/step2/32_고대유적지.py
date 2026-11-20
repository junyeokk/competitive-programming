import heapq

INF = 10000000

h, w = map(int, input().split())

uArr = [[0 for i in range(w + 2)] for j in range(h + 2)]
arr = []
for i in range(h):
    arr.append(list(map(int, input().split())))

for i in range(h):
    for j in range(w):
        uArr[i + 1][j + 1] = arr[i][j]

uArr[0][0] = 9
uArr[1][0] = 9
uArr[0][1] = 9

uArr[h + 1][w + 1] = 9
uArr[h][w + 1] = 9
uArr[h + 1][w] = 9

starty = 0
startx = w + 1
pq = []
cost = [[INF for i in range(w + 2)] for j in range(h + 2)]

cost[starty][startx] = 0
heapq.heappush(pq, (0, startx, starty))

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

while pq:
    c, x, y = heapq.heappop(pq)
    if cost[y][x] < c:
        continue

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx > w + 1 or ny < 0 or ny > h + 1:
            continue
        if uArr[ny][nx] == 9:
            continue
        if cost[ny][nx] > cost[y][x] + uArr[ny][nx]:
            cost[ny][nx] = cost[y][x] + uArr[ny][nx]
            heapq.heappush(pq, (cost[ny][nx], nx, ny))

if cost[h + 1][0] == INF:
    print('IMPOSSIBLE')
else:
    print(cost[h + 1][0])