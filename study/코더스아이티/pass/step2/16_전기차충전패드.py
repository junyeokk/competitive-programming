n = int(input())

carr = []
menu = []
ans = 15 * 200000

for i in range(n):
    carr.append(list(map(int, input().split())))

for y in range(n):
    for x in range(n):
        menu.append((x, y))

def solve(arr):
    point = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in arr:
        x, y = menu[i]
        point.append((x, y))
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            point.append((nx, ny))
    
    v = set(point)
    if len(v) != 15:
        return
    
    for p in point:
        if p[0] < 0 or p[0] >= n or p[1] < 0 or p[1] >= n:
            return
    
    cost = 0
    for p in point:
        cost += carr[p[1]][p[0]]
    global ans
    ans = min(ans, cost)

for a in range(n * n - 2):
    for b in range(a + 1, n * n - 1):
        for c in range(b + 1, n * n):
            solve([a, b, c])

print(ans)