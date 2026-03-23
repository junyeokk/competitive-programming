n, l, k = map(int, input().split())

sc = []
res = 0

for i in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        sc.append(140)
    elif sub1 <= l:
        sc.append(100)

sc = sorted(sc, reverse = True)

for i in range(min(len(sc), k)):
    res += sc[i]

print(res)