n, m = map(int, input().split())

arr = []
for i in range(n):
    v = int(input())
    arr.append(v)

low = max(arr)
high = sum(arr)
while low <= high:
    mid = (low + high) // 2
    
    cnt = 1
    b = mid # 배터리 남은 양
    for v in arr:
        if b >= v:
            b -= v
        else:
            b = mid
            b -= v
            cnt += 1

    if cnt <= m:
        high = mid - 1
        ans = mid
    else:
        low = mid + 1

print(ans)