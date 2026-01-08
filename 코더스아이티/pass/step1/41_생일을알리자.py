n = int(input())

gp = [[]]
visit = []
ans = []
max = 0
cnt = 0

for i in range(1, n + 1):
    s = list(map(int, input().split()))
    gp.append(s[1:])

def dfs(v):
    global cnt
    cnt += 1
    visit[v] = True
    
    for w in gp[v]:
        if visit[w] == False:
            dfs(w)

for i in range(1, n + 1):
    visit = [False for _ in range(n + 1)]
    cnt = 0
    dfs(i)
    
    if max < cnt:
        max = cnt
        ans.clear()
        ans.append(i)
    elif max == cnt:
        ans.append(i)

for a in ans:
    print(a, end = ' ')