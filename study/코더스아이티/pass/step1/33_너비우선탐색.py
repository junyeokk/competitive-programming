from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n):
    graph[i + 1] .sort()

q = deque()
visit = [0 for i in range(n + 1)]

q.append(v)
visit[v] = 1
print(v, end = ' ')

while q:
    t = q.popleft()
    
    for w in graph[t]:
        if visit[w] == 0:
            visit[w] = 1
            print(w, end = ' ')
            q.append(w)
        
