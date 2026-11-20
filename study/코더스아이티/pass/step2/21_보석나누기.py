n, m = map(int, input().split())

arr = []
for i in range(m):
    arr.append(int(input()))

low = 1
high = max(arr)
while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for v in arr:
        cnt += v // mid
        cnt += 1 if v % mid != 0 else 0
    
    if n < cnt:
        low = mid + 1
    else:
        high = mid - 1
        ans = mid

print(ans)