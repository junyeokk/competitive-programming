h, w = map(int, input().split())

arr = []

for i in range(h):
    s = list(map(int, input().split()))
    arr.append(s)

q = int(input())
for i in range(q):
    t, v = map(int, input().split())
    if t == 0:
        print(*arr[v])
    else:
        for j in range(h):
            print(arr[j][v], end = ' ')
        print()