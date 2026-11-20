from collections import defaultdict

s = input()
cnt = defaultdict(int)
res = ''

for ch in s:
    cnt[ch] += 1

u, d, p, c = cnt['U'], cnt['D'], cnt['P'], cnt['C']

if u + c > (d + p + 1) // 2:
    res += 'U'
if d + p >= 1:
    res += 'DP'
if not res:
    res += 'C'

print(res)