fibs = []
fibs.append(1)
fibs.append(2)

while fibs[-1] < 10 ** 100:
    fibs.append(fibs[-1] + fibs[-2])

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    count = 0
    for f in fibs:
        if a <= f <= b:
            count += 1
    print(count)