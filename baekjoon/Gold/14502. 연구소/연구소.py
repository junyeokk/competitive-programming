from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

blanks = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            blanks.append((i, j))

best = 0
for walls in combinations(blanks, 3):
    tmp = copy.deepcopy(grid)
    for x, y in walls:
        tmp[x][y] = 1

    q = deque()
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                count += 1
    best = max(best, count)

print(best)