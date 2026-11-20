from itertools import combinations
from collections import deque

def bfs(startArr):
    q = deque()
    visit = [[0 for i in range(n)] for j in range(n)]
    for c in startArr:
        q.append(c)
        visit[c[1]][c[0]] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    tDist = 0
    hCnt = 0

    while q:
        t = q.popleft()
        dist = t[2]
        for i in range(4):
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[ny][nx] == 0 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                q.append((nx, ny, dist + 1))
            if arr[ny][nx] == 3 and visit[ny][nx] == 0:
                tDist += dist + 1
                hCnt += 1
                visit[ny][nx] = 1
    if hCnt == houseCnt:
        return tDist
    else:
        return -1

n, m = map(int, input().split())

arr = []
sPosArr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

houseCnt = 0

for y in range(n):
    for x in range(n):
        if arr[y][x] == 2:
            sPosArr.append((x, y, 0))
        elif arr[y][x] == 3:
            houseCnt += 1


comb = combinations(sPosArr, m)
ans = []

for v in comb:
    t = bfs(v)
    if t != -1:
        ans.append(t)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))