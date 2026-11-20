from collections import deque

# L R U D
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(grid, start_x, start_y):
  n, m = len(grid), len(grid[0])
  visited = [[-1 for _ in range(m)] for _ in range(n)]

  queue = deque([(start_x, start_y)])
  visited[start_x][start_y] = 0

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 1 and visited[nx][ny] == -1:
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))
      
    return visited