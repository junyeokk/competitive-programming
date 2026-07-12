def calCost(a, b):
    cost = 0
    for i in range(k):
        cost += abs(ord(a[i]) - ord(b[i]))
    return cost

n, k = map(int, input().split())

arr = []
for i in range(n):
    s = input().strip()
    arr.append(s)

edge = []
for i in range(n):
    for j in range(i + 1, n):
        edge.append((calCost(arr[i], arr[j]), i, j))

edge.sort()

p = [i for i in range(n)]
def find(x):
    if p[x] == x:
        return p[x]
    p[x] = find(p[x])
    return p[x]

for e in edge:
    p1 = find(e[1])
    p2 = find(e[2])
    if p1 != p2:
        p[p1] = p2
        ans = e[0]

print(ans)