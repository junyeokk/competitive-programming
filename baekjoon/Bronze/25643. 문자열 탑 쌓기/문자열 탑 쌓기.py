n, m = map(int, input().split())

prev = ''

for i in range(n):
    s = input()
    if i == 0:
        prev = s
        continue
    else:
        found = False
        for d in range(-(m-1), m):
            start = max(0, d)
            end = min(m - 1, d + m - 1)
            ok = True
            for p in range (start, end + 1):
                if prev[p] != s[p - d]:
                    ok = False
                    break
            if ok:
                found = True
                break
        if not found:
            print(0)
            exit()
    prev = s
print(1)