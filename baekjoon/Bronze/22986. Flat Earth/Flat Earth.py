t = int(input())

def solve():
    res = 0
    n, k = map(int, input().split())

    if k >= n:
        res = 4 * n * (n + 1) // 2
    else:
        res = 4 * (n * (n + 1) // 2 - (n - k - 1) * (n - k) // 2)

    print(res)


for i in range(t): 
    solve()