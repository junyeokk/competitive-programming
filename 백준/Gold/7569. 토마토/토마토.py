from collections import deque

m, n, h = map(int, input().split())
q = deque()
ans = -1

arr = []
for k in range(h):
    layer = []
    for i in range(n):
        layer.append(list(map(int, input().split())))
    arr.append(layer)

dist = [[[-1] * m for i in range(n)] for _ in range(h)]

def bfs():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    
    while(q):
        z, y, x = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if arr[nz][ny][nx] == 0 and dist[nz][ny][nx] == -1:
                    dist[nz][ny][nx] = dist[z][y][x] + 1
                    q.append((nz, ny, nx))

for k in range(h):
    for j in range(n):
        for i in range(m):
            if arr[k][j][i] == 1:
                q.append((k, j, i))
                dist[k][j][i] = 0

bfs()

for k in range(h):
    for j in range(n):
        for i in range(m):
            if arr[k][j][i] == 0 and dist[k][j][i] == -1:
                print(-1)
                exit()
            ans = max(ans, dist[k][j][i])

print(ans)