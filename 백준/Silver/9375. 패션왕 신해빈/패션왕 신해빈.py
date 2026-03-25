from collections import defaultdict

t = int(input())

def solve():
    d = defaultdict(int)
    n = int(input())
    for i in range(n):
        s = input().split()
        d[s[1]] += 1

    res = 1
    for v in d.values():
        res *= (v + 1)
    print(res - 1)


for i in range(t):
    solve()