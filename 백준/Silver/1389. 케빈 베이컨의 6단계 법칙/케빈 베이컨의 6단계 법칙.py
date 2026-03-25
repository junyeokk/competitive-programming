n, m = map(int, input().split())

arr = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]

for i in range(n + 1):
    arr[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

res = float('inf')
ans = 0
for i in range(1, n + 1):
    t = sum(arr[i][1:n+1])
    if t < res:
        res = t
        ans = i
print(ans)