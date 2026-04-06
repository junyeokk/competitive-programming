n, m = map(int, input().split())

s = list(map(int, input().split()))
s = sorted(s)

visited = [False] * n

def solve(depth, path):
    if depth == m:
        print(*path)
        return
    for i in range(n):
        if visited[i]:
            continue
        if i > 0 and s[i] == s[i - 1] and not visited[i - 1]:
            continue
        visited[i] = True
        solve(depth + 1, path + [s[i]])
        visited[i] = False

solve(0, [])