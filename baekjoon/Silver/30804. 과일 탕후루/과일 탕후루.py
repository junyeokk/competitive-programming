from collections import defaultdict

n = int(input())
s = list(map(int, input().split()))

d = defaultdict(int)
left = 0
res = 0

for right in range(n):
    d[s[right]] += 1

    while len(d) > 2:
        d[s[left]] -= 1
        if d[s[left]] == 0:
            del d[s[left]]
        left += 1
    
    res = max(res, right - left + 1)

print(res)