n, k = map(int, input().split())

memo = [0 for i in range(1001)]
memo[0] = 1
memo[1] = 1

for i in range(2, 1001):
    memo[i] = memo[i - 1] * i

res = memo[n] // (memo[k] * memo[n - k])
rstring = str(res)
cnt = 0
for rs in rstring:
    if rs == '0':
        cnt += 1

print(cnt)