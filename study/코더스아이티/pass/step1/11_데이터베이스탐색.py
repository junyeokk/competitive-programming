n, m = map(int, input().split())

data = []
for i in range(n):
    s = list(map(int, input().split()))
    data.append(s)

q = int(input())

def isEqual(a, b):
    for i in range(m):
        if b[i] == -1:
            continue
        if a[i] != b[i]:
            return False
    return True
    

for i in range(q):
    res = 0
    s = list(map(int, input().split()))
    for d in data:
        if isEqual(d, s) == True:
            res += 1
    print(res)
        