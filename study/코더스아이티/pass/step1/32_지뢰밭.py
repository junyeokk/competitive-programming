dx = [0, 1, 0 , -1]
dy = [-1, 0, 1, 0]

w, h = map(int, input().split())

graph = []

for i in range(h):
    s = list(map(int, input().split()))
    graph.append(s)

q = int(input())

for i in range(q):
    x, y = map(int, input().split())
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if nx < 0 or nx >= w or ny < 0 or ny >= h:
            print(0, end = ' ')
        else:
            print(graph[ny][nx] + 1, end = ' ')
    print()