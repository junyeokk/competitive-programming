import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = []
q = deque()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dist = [[-1] * m for i in range(n)]

def bfs():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and dist[nx][ny] == -1:
                if arr[nx][ny] != 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


for i in range(n):
    s = list(map(int, input().split()))
    arr.append(s)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i, j))
            dist[i][j] = 0

bfs()

for i in range(n):
    row = []
    for j in range(m):
        if arr[i][j] == 0:
            row.append(0)
        else:
            row.append(dist[i][j])
    print(*row)