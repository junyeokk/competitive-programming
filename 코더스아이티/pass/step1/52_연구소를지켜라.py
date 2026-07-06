from collections import deque
from itertools import combinations

def bfs(start):
    q = deque(virus)
    visit = [[0 for i in range(m)] for j in range(n)]

    for v in start:
        x, y = v
        visit[y][x] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visit[ny][nx] == 0 and arr[ny][nx] == 0:
                visit[ny][nx] = 1
                cnt += 1
                q.append((nx, ny))
        
    return cnt

n, m = map(int, input().split()) # n 세로

arr = []
for i in range(n):
    s = list(map(int, input().split()))
    arr.append(s)

menu = []
virus = []
for y in range(n):
    for x in range(m):
        if arr[y][x] == 0:
            menu.append((x, y))
        elif arr[y][x] == 2:
            virus.append((x, y))

ans = []
for v in combinations(menu, 3):
    ans.append(len(menu) - 3 - bfs(v))

print(max(ans))