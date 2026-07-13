a, b, pa, pb, n = map(int, input().split())

ans = 0
for x in range(n // pa + 1):
    c = n - x * pa
    y = c // pb
    ans = max(ans, a * x  + b * y)

print(ans)