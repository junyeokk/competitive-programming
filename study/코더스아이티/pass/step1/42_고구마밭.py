from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque()
    gp[y][x] = 0
    q.append((x, y))
    
    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if gp[ny][nx] == 1:
                gp[ny][nx] = 0
                q.append((nx, ny))

def solve():
    global m, n, gp
    m, n, k = map(int, input().split())
    gp = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(k):
        x, y = map(int, input().split())
        gp[y][x] = 1
    
    res = 0
    for y in range(n):
        for x in range(m):
            if gp[y][x] == 1:
                bfs(x, y)
                res += 1
    print(res)


t = int(input())

for i in range(t):
    solve()