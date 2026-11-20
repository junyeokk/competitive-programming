LEFT = 6
RIGHT = 2
arr = []

for i in range(4):
    t = list(map(int, list(input())))
    arr.append(t)

k = int(input())
for i in range(k):
    n, v = map(int, input().split())
    ans = [0, 0, 0, 0]
    ans[n - 1] = v
    # 왼쪽
    for j in range(n - 2, -1, -1):
        if arr[j][RIGHT] != arr[j + 1][LEFT]:
            ans[j] = -ans[j + 1]
        else:
            break

    # 오른쪽
    for j in range(n, 4):
        if arr[j][LEFT] != arr[j - 1][RIGHT]:
            ans[j] = -ans[j - 1]
        else:
            break

    for j in range(4):
        if ans[j] == 1: # 시계방향
            arr[j] = arr[j][7:] + arr[j][:7]
        elif ans[j] == -1: # 반시계방향
            arr[j] = arr[j][1:] + arr[j][:1]

res = 0
for i in range(4):
    res += arr[i][0] * 2 ** i

print(res)