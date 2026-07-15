n, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

def count(m):
    lastPos = 0
    cnt = 1
    for i in range(1, n):
        if arr[i] - arr[lastPos] >= m:
            cnt += 1
            lastPos = i
    
    return cnt

low = 1
high = arr[-1]
ans = 0

while low <= high:
    mid = (low + high) // 2
    chkc = count(mid)
    if chkc >= c: 
        ans = max(ans, mid)
        low = mid + 1
    else:
        high = mid - 1

print(ans)