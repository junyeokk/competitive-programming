h, w = map(int, input().split())

arr = []

for i in range(h):
    s = list(map(int, input().split()))
    s.append(1)
    arr.append(s)

arr.append([1 for _ in range(w + 1)])

x = 0
y = 0
res = 0
while True:
    arr[y][x] = -1
    if arr[y][x + 1] == 0:
        x += 1
        continue
    if arr[y][x + 1] == 2:
        x += 1
        res += 2
        continue
    if arr[y + 1][x] == 0:
        y += 1
        continue
    if arr[y + 1][x] == 2:
        y += 1
        res += 2
        continue
    break
print(res)

for i in range(h):
    for j in range(w):
        if arr[i][j] == -1:
            print("*", end = ' ')
        else:
            print(arr[i][j], end = ' ')
    print()