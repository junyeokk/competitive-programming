n = int(input())

data = []
for i in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

min_rss = float('inf')
min_a = -1
min_b = -1

for b in range(1, 101):
    for a in range(1, 101):
        rss = 0
        for x, y in data:
            rss += (y - (a * x + b)) ** 2
        if rss < min_rss:
            min_rss = rss
            min_a = a
            min_b = b

print(min_a, min_b)