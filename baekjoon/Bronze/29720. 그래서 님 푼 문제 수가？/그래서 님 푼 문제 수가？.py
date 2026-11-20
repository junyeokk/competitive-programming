n, m, k = map(int, input().split())

p = n - (m * k)
q = n - (m * (k - 1)) - 1

if p < 0: p = 0
if q < 0: q = 0
print(p, q)