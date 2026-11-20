from collections import deque

n, h, l = map(int, input().split())
hl = list(map(int, input().split()))
q = deque()
dist = [10**10] * n
graph = [[] for i in range(n)]

for i in range(l):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for mov in hl:
    dist[mov] = 0
    q.append(mov)

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == 10**10:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

maxh = -1
idx = -1
for i in range(n):
    if maxh < dist[i]:
        maxh = dist[i]
        idx = i

print(idx)
