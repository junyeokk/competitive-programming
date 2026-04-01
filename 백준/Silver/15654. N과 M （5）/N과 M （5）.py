n, m = map(int, input().split())
s = list(map(int, input().split()))
s = sorted(s)

result = []
used = [False] * n

def perm(depth):
    if depth == m:
        print(*result)
        return
    for i in range(n):
        if not used[i]:
            used[i] = True
            result.append(s[i])
            perm(depth + 1)
            result.pop()
            used[i] = False

perm(0)