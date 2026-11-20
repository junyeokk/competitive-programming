n, m = map(int, input().split())

s = list(map(int, input().split()))
s = sorted(s)

def solve(depth, path, start):
    if depth == m:
        print(*path)
        return
    for i in range(start, n):
        if i > start and s[i] == s[i - 1]:
            continue
        solve(depth + 1, path + [s[i]], i)

solve(0, [], 0)