s = input().split('-')
s_t = []
res = 0

for t in s:
    sm = 0
    for v in t.split('+'):
        sm += int(v)
    s_t.append(sm)

res += s_t[0]
for i in range(1, len(s_t)):
    res -= s_t[i]

print(res)