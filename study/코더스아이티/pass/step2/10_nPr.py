n, r = map(int, input().split())
ans = []
visit = [0 for i in range(n + 1)]

def perm(idx):
    if idx == r + 1:
        print(ans)
        return
    
    for i in range(1, n + 1):
        if visit[i] == 0:
            ans.append(i)
            visit[i] = 1
            perm(idx + 1)
            visit[i] = 0
            ans.pop()

perm(1)