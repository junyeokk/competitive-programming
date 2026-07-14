def solve():
    n, m, v = map(int, input().split())
    edge = []
    INF = 50000000
    dist = [INF for i in range(n + 1)]
    for i in range(m):
        s, e, w = map(int, input().split())
        edge.append((s, e, w))
        edge.append((e, s, w))
    
    for i in range(v):
        s, e, w = map(int, input().split())
        edge.append((s, e, -w))

    for i in range(n - 1):
        for s, e, w in edge:
            if dist[e] > dist[s] + w:
                dist[e] = dist[s] + w
    
    for s, e, w in edge:
        if dist[e] > dist[s] + w:
            print("YES")
            return

    print("NO")

tc = int(input())
for i in range(tc):
    solve()