from collections import defaultdict
n = int(input())

s = list(map(int, input().split()))
ss = sorted(s)

arr = defaultdict(int)

cnt = 0

for i in range(1, len(ss)):
    if ss[i] != ss[i - 1]:
        cnt += 1
    arr[ss[i]] = cnt

print(*[arr[i] for i in s])