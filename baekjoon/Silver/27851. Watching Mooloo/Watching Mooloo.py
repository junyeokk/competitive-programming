n, k = map(int, input().split())

days = list(map(int, input().split()))
res = 1 + k # 첫 날 구독

for i in range(1, len(days)):
    diff = days[i] - days[i - 1]
    res += min(diff, 1 + k)

print(res)