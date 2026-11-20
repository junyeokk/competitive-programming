n, m, v = map(int, input().split())
graph = [[] for _ in range(m + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n + 1):
    graph[i].sort()

visit = [0 for _ in range(n + 1)]

def dfs(v):
    visit[v] = 1
    print(v, end = ' ')
    for w in graph[v]:
        if visit[w] == 0:
            dfs(w)

dfs(v)
    