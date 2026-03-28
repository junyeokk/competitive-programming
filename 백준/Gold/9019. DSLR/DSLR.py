import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def dslr(n, q):
    if q == 'D':
        return (n * 2) % 10000
    elif q == 'S':
        return (n - 1) % 10000
    elif q == 'L':
        return (n % 1000) * 10 + n // 1000
    elif q == 'R':
        return (n // 10) + (n % 10) * 1000

def solve():
    a, b = map(int, input().split())
    d = deque()
    d.append(a)
    prev = [-1] * 10000
    how = [''] * 10000
    prev[a] = a
    
    while d:
        n = d.popleft()
        if n == b:
            # 역추적
            path = []
            while n != a:
                path.append(how[n])
                n = prev[n]
            print(''.join(reversed(path)))
            return
        for q in "DSLR":
            nn = dslr(n, q)
            if prev[nn] == -1:
                prev[nn] = n 
                how[nn] = q
                d.append(nn)

for i in range(t):
    solve()