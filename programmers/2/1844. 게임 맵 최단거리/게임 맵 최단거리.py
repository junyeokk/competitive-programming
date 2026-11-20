from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])

    dq = deque()
    dq.append((0, 0))
    
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and maps[nx][ny] == 1 and dist[nx][ny] == 0:
                dq.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
    
    answer = dist[-1][-1] if dist[-1][-1] != 0 else -1
    
    return answer