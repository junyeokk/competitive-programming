n, m = map(int, input().split())

arr = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

c = []
live = [0 for i in range(n + 1)]

for i in range(n):
    c.append(int(input()))
c.reverse()

p = [i for i in range(n + 1)]
def find(v):
    if p[v] == v:
        return p[v]

    p[v] = find(p[v])
    return p[v]

ans = []
con = 0

for i in range(n):
    v = c[i]
    live[v] = 1
    for u in arr[v]:
        if live[u] == 1:
            pv = find(v)
            pu = find(u)
            if pv != pu:
                p[pv] = pu
                con += 1
    if i == con:
        ans.append('YES')
    else:
        ans.append('NO')

ans.reverse()
for v in ans:
    print(v)