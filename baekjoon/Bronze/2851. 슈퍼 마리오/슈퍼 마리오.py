sums = [0]
t = 0
res = 0

for i in range(10):
    t += int(input())
    sums.append(t)

for s in sums:
    if abs(100 - res) >= abs(100 - s):
        res = s

print(res)