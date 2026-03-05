n, m = map(int, input().split())

water = [0 for i in range(n + 1)]
graph = [[] for i in range(n + 1)]
water[1] = 100

for i in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)

for i in range(1, n + 1):
    hos = len(graph[i])
    if water[i] and hos > 0:
        for dx in graph[i]:
            water[dx] += water[i] / hos
        water[i] = 0

print(max(water))