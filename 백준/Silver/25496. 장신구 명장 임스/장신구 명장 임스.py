p, n = map(int, input().split())
s = list(map(int, input().split()))

s = sorted(s)
cnt = 0
idx = 0

while idx < n:
    if 200 - p > 0:
        cnt += 1
        p += s[idx]
    else:
        break
    idx += 1

print(cnt)