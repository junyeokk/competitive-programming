result = []

n, m = map(int, input().split())

def comb(depth, start):
    if depth == m:
        print(*result)
        return
    for i in range(start, n + 1):
        result.append(i)
        comb(depth + 1, i)
        result.pop()

comb(0, 1)