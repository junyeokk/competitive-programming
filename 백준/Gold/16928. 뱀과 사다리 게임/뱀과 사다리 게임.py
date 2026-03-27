from collections import deque

n, m = map(int, input().split())

dist = [-1] * 101
dist[1] = 0
move = {}

dq = deque()

for i in range(n):
    x, y = map(int, input().split())
    move[x] = y

for i in range(m):
    u, v = map(int, input().split())
    move[u] = v

def bfs():
    while dq:
        x = dq.popleft()
        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue
            if nx in move: # 뱀, 사다리 이동
                nx = move[nx]
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                dq.append(nx)    

dq.append(1)
bfs()
print(dist[100])