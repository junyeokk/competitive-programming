n = int(input())

ls = []

for i in range(n):
    s, t = map(int, input().split())
    ls.append((s, t))

ls = sorted(ls)

e = 0
for s, t in ls:
    e = max(e, s) + t

print(e)