import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = 1

if n >= m:
    print(0)
else:
    for i in range(2, n + 1):
        res = res * i % m
    print(res)