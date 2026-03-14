from collections import defaultdict

n = int(input())
d = defaultdict(int)
count = 0

for i in range(n):
    s, p = map(str, input().split())
    if p == '+':
        d[s] += 1
    elif p == '-':
        if d[s] > 0:
            d[s] -= 1
        elif d[s] == 0:
            count += 1

for v in d.values():
    if v > 0:
        count += v

print(count)