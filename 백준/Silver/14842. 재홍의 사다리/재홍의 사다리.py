w, h, n = map(int, input().split())

total = 0
for k in range(1, n):
    x = k * w / n
    y1 = (h / w) * x
    y2 = -1 * (h / w) * x + h
    total += abs(y1 - y2)

print(f"{total:.6f}")