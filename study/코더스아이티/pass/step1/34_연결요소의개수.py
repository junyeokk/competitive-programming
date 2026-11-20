n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def dfs(v):
    visit[v] = True
    
    for w in arr[v]:
        if visit[w] == False:
            dfs(w)

cnt = 0
for i in range(1, n + 1):
    if visit[i] == False:
        dfs(i)
        cnt += 1

print(cnt)