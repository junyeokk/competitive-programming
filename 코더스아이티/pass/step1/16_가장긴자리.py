h, w = map(int, input().split())

arr = []

for i in range(h):
    s = list(map(int, input().split()))
    arr.append(s)

ans = 0

# 가로
for i in range(h):
    res = 0
    for j in range(w):
        if arr[i][j] == 0:
            res += 1
            ans = max(ans, res)
        else:
            res = 0

# 세로
for i in range(w):
    res = 0
    for j in range(h):
        if arr[j][i] == 0:
            res += 1
            ans = max(ans, res)
        else:
            res = 0

print(ans)