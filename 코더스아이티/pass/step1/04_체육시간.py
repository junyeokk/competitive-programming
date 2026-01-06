n = int(input())

arr = []

for i in range(n):
    name, a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    arr.append([name, a, b, c])

arr.sort(key = lambda v: (v[1], v[1] + v[2] + v[3]), reverse = True)
for v in arr:
    print(v[0])
print()

arr.sort(key = lambda v: (v[2], v[1] + v[2] + v[3]), reverse = True)
for v in arr:
    print(v[0])
print()

arr.sort(key = lambda v: (v[3], v[1] + v[2] + v[3]), reverse = True)
for v in arr:
    print(v[0])
print()