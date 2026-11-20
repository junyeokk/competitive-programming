import sys
sys.setrecursionlimit(100007)
input = sys.stdin.readline

n = int(input())

p = [i for i in range(2 * n + 1)]
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

d = {}
number = 0

for i in range(n):
    a, b, c = input().split()
    for name in (a, c):
        if name not in d:
            d[name] = number
            number += 1
    p1, p2 = find(d[a]), find(d[c])
    if p1 != p2:
        p[p1] = p2

m = int(input())
for i in range(m):
    a, b = input().split()
    if find(d[a]) == find(d[b]):
        print('Related')
    else:
        print('Not Related')