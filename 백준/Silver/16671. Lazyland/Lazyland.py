from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

jobs = defaultdict(list)

for i in range(n):
    jobs[a[i]].append(b[i])

pool = []
need = 0

for j in range(1, k + 1):
    if len(jobs[j]) == 0:
        need += 1
    else:
        jobs[j].sort()
        pool.extend(jobs[j][:-1])

pool.sort()
print(sum(pool[:need]))