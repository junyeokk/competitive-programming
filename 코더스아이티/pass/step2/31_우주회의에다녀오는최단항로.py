import heapq

n, m, x = map(int, input().split())
arr = [[] for i in range(n + 1)] # 정방향 인접리스트
INF = 10000000

for i in range(m):
    s, e, c = map(int, input().split())
    arr[s].append((e, c)) # 다익스트라 한 번

def dijkstra(start):
    cost = [INF for i in range(n + 1)]
    cost[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        t = heapq.heappop(pq)
        if cost[t[1]] < t[0]:
            continue
        
        for w in arr[t[1]]:
            if cost[w[0]] > cost[t[1]] + w[1]:
                cost[w[0]] = cost[t[1]] + w[1]
                heapq.heappush(pq, (cost[w[0]], w[0]))

    return cost

cost = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    c = dijkstra(i)
    if i == x:
        for j in range(1, n + 1):
            cost[j] += c[j]
    else:
        cost[i] += c[x]

print(max(cost))