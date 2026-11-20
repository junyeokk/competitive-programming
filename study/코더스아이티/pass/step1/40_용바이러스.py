n = int(input())
k = int(input())

gp = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]
cnt = 0

def dfs(v):
    global cnt
    cnt += 1
    visit[v] = True
    
    for w in gp[v]:
        if visit[w] == False:
            dfs(w)

for i in range(k):
    s, e = map(int, input().split())
    gp[s].append(e)
    gp[e].append(s)

dfs(1)
print(cnt)
