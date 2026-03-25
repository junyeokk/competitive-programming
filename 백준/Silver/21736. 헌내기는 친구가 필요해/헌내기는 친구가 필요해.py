from collections import deque

n, m = map(int, input().split())

arr = []
dq = deque()
cnt = 0

for i in range(n):
    s = list(input())
    arr.append(s)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            dq.append((i, j))
            arr[i][j] = 'X'

def bfs():
    global cnt
    while dq:
        x, y = dq.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 'X':
                if arr[nx][ny] == 'P':
                    cnt += 1
                arr[nx][ny] = 'X'
                dq.append((nx, ny))

bfs()

print(cnt if cnt > 0 else 'TT')