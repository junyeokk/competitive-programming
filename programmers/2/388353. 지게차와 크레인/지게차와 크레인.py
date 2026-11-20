from collections import deque

def solution(storage, requests):
    grid = [list(row) for row in storage]
    n = len(grid)
    m = len(grid[0])
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    def check(x, y, air):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or air[nx][ny]:
                return True
        return False
    
    def get_air():
        air = [[False] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == '.':
                    air[i][j] = True
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not air[nx][ny] and grid[nx][ny] == '.':
                    air[nx][ny] = True
                    q.append((nx, ny))
        return air

    for r in requests:
        alpha = r[0]
        if len(r) == 2: # 크레인
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == alpha:
                        grid[i][j] = '.'
        else: # 지게차
            air = get_air()
            remove = []
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == alpha and check(i, j, air):
                        remove.append((i, j))
            for i, j in remove:
                grid[i][j] = '.'

    
    return n * m - sum(row.count('.') for row in grid)