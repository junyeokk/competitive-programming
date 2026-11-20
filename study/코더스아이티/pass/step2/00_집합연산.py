import sys
sys.setrecursionlimit(100005)

n, m = map(int, input().split())

p = [i for i in range(n + 1)]

def find(x):
    if p[x] != x:
        return find(p[x])
    return x

def union(x, y):
    r1 = find(x)
    r2 = find(y)
    p[r1] = r2

for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print(1)
        else:
            print(0)