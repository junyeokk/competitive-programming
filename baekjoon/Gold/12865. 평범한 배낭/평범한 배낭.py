n, k = map(int, input().split())
items = []

for i in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = items[i - 1]
    for j in range(k + 1):
        if j >= w:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])