n, k = map(int, input().split())

arr = []
for i in range(k):
    a, b = map(int, input().split())
    arr.append(a * b)

arr.sort(reverse = True)

for i in range(k):
    n -= arr[i]
    if n <= 0:
        print(i + 1)
        break