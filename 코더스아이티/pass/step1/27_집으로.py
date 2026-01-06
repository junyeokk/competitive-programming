from collections import deque

q = deque()
n, k = map(int, input().split())
res = []

for i in range(n):
    q.append(i + 1)

for i in range(n):
    for j in range(k - 1):
        t = q.popleft()
        q.append(t)
    res.append(q.popleft())

for r in res:
    print(r, end = ' ')