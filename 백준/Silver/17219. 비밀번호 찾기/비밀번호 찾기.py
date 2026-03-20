from collections import defaultdict
import sys
input = sys.stdin.readline

d = defaultdict(str)

n, m = map(int, input().split())

for i in range(n):
    adr, pw = map(str, input().split())
    d[adr] = pw

for i in range(m):
    t = input().strip()
    print(d[t])