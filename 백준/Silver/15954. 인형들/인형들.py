import math

n, k = map(int, input().split())
s = list(map(int, input().split()))

ps = [0] * (n + 1)
psq = [0] * (n + 1)

for i in range(n):
    ps[i + 1] = ps[i] + s[i]
    psq[i + 1] = psq[i] + s[i] ** 2

min_std = float('inf')

for length in range(k, n + 1):
    for i in range(n - length + 1):
        ts = ps[i + length] - ps[i]
        tsq = psq[i + length] - psq[i]
        numerator = tsq * length - ts ** 2
        std = math.sqrt(numerator) / length
        min_std = min(min_std, std)

print(min_std)