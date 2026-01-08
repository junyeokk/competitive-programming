n = int(input())

arr = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    s = list(map(int, list(input())))
    arr.append(s)

def dfs(y, x):
    arr[y][x] = 0
    cnt = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if arr[ny][nx] == 1:
            cnt += dfs(ny, nx)
            
    return cnt

ans = []
for y in range(n):
    for x in range(n):
        if arr[y][x] == 1:
            cnt = dfs(y, x)
            ans.append(cnt)

ans.sort()
print(len(ans))
for a in ans:
    print(a)