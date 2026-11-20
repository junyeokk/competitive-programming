n = int(input())

arr = []
mins = 10 ** 18
for i in range(n):
    s = int(input())
    arr.append(s)

arr = sorted(arr)
for i in range(len(arr) // 2):
    if mins > arr[i] + arr[len(arr) - i - 1]:
        mins = arr[i] + arr[len(arr) - i - 1]

print(mins)