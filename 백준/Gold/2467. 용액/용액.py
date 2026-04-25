n = int(input())
s = list(map(int, input().split()))

left = 0
right = n - 1
best = float('inf')
ansl, ansr = 0, 0

while left < right:
    total = s[left] + s[right]

    if abs(total) < best:
        best = abs(total)
        ansl, ansr = s[left], s[right]
    
    if total > 0:
        right -= 1
    elif total < 0:
        left += 1
    else:
        break

print(ansl, ansr)