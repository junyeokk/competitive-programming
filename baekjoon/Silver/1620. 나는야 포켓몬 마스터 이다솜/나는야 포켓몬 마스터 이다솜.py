import sys
input = sys.stdin.readline

from collections import defaultdict

n, m = map(int, input().split())

ndic = defaultdict(int)
vdic = defaultdict(str)

for i in range(n):
    s = input().strip()
    idx = i + 1
    ndic[idx] = s
    vdic[s] = idx

for i in range(m):
    t = input().strip()
    if t.isdigit():
        print(ndic[int(t)])
    else:
        print(vdic[t])