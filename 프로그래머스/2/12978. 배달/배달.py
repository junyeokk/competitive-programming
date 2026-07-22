import heapq

def solution(N, road, K):
    answer = 0
    INF = float('inf')
    dist = [INF] * (N + 1)
    visit = [False] * (N + 1)
    q = []
    
    g = [[] for _ in range(N + 1)]
    for r in road:
        a, b, c = r
        g[a].append((c, b))
        g[b].append((c, a))
    
    heapq.heappush(q, (0, 1))
    dist[1] = 0
    
    while q:
        cost, u = heapq.heappop(q)
        if visit[u]:
            continue
        visit[u] = True
        for w, t in g[u]:
            if cost + w < dist[t]:
                dist[t] = dist[u] + w
                heapq.heappush(q, (dist[t], t))
    
    answer = sum(d <= K for d in dist[1:])
    
    return answer