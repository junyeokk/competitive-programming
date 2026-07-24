from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(place, x, y):
    q = deque()
    visited = [[False] * 5 for _ in range(5)]
    
    q.append((x, y, 0))
    visited[x][y] = True
    
    while q:
        x, y, dist = q.popleft()
        if dist == 2:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < 5 and ny < 5:
                if visited[nx][ny]:
                    continue
                if place[nx][ny] == 'X':
                    continue
                if place[nx][ny] == 'P':
                    return False
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
    
    return True

def solution(places):
    answer = []
    for p in places:
        valid = True        
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    if not bfs(p, i, j):
                        valid = False
        answer.append(1 if valid else 0)
    return answer