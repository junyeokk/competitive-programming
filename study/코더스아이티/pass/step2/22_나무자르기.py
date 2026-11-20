n, m = map(int, input().split())
arr = list(map(int, input().split()))

low = 0
high = max(arr)

while low <= high:
    mid = (low + high) // 2
    s = 0

    for v in arr:
        s += max(v - mid, 0) # max 시간초과 나면 if문으로 대체
    
    if s >= m:
        low = mid + 1
        ans = mid
    else:
        high = mid - 1

print(ans)