import sys
sys.setrecursionlimit(10001)
w, h = map(int, input().split())

arr = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(y, x, original, new):
    arr[y][x] = new
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and arr[ny][nx] == original:
            dfs(ny, nx, original, new)

for i in range(h):
    s = list(map(int, input().split()))
    arr.append(s)

n = int(input())
for i in range(n):
    x, y, new = map(int, input().split())
    original = arr[y][x]
    if original != new:
        dfs(y, x, original, new)

for y in range(h):
    for x in range(w):
        print(arr[y][x], end = ' ')
    print()