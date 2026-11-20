import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())

p = [i for i in range(n + 1)]

def find(x):
    if p[x] == x:
        return p[x]
    p[x] = find(p[x])
    return p[x]

for i in range(m):
    arr = list(map(int, input().split()))
    for j in range(n):
        p1 = find(arr[j])
        p2 = find(j + 1)
        if p1 != p2:
            p[p1] = p2

for i in range(q):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print("YES")
    else:
        print("NO")