import sys
sys.setrecursionlimit(100007)

n, m = map(int, input().split())
edge = []
p = [i for i in range(n + 1)]

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    r1 = find(x)
    r2 = find(y)
    p[r1] = r2

for i in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort()
ans = 0
for e in edge:
    if find(e[1]) != find(e[2]):
        union(e[1], e[2])
        ans += e[0]

print(ans)