from collections import deque

n = int(input())
arr = []
q = deque()

visit = [[False] * n for i in range(n)]

def bfs(sx, sy):
    q.append((sx, sy))
    visit[sx][sy] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] and not visit[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = True

for i in range(n):
    arr.append(list(input()))

cnt = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i, j)
            cnt += 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

pcnt = 0
visit = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i, j)
            pcnt += 1

print(cnt, pcnt)