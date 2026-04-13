n, k = map(int, input().split())
arr = []

left = 0
answer = 0

for i in range(n):
    arr.append(int(input()))

arr = sorted(arr)
for right in range(n):
    while arr[right] - arr[left] > k:
        left += 1
    answer = max(answer, right - left + 1)

print(answer)