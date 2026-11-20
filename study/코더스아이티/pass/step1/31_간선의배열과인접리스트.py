a, b = map(int, input().split())

res = [[] for _ in range(b + 1)]

for i in range(a):
    x, y = map(int, input().split())
    
    res[x].append(y)
    res[y].append(x)

for i in range(b):
    res[i + 1].sort()
    print(i + 1, ":", res[i + 1])
