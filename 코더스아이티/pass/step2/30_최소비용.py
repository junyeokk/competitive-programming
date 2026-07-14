import heapq

v, e = map(int, input().split())
INF = 20000 * 100

start = int(input())
g = [[] for i in range(v + 1)]
dist = [INF for i in range(v + 1)]
visit = [False for i in range(v + 1)]

for i in range(e):
    s, e, c = map(int, input().split())
    g[s].append((e, c))

q = []
heapq.heappush(q, (0, start))
dist[start] = 0

while q:
    cost, u = heapq.heappop(q)
    if visit[u] == True:
        continue
    
    visit[u] = True
    for t, w in g[u]:
        if cost + w < dist[t]:
            dist[t] = dist[u] + w
            heapq.heappush(q, (dist[t], t))

for i in range(1, v + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])