s = input()

cnt = 0
res = 0
prev = ''

for c in s:
    if c == '(':
        cnt += 1
    else:
        cnt -= 1
        if prev == '(':
            res += cnt
        else:
            res += 1
    prev = c

print(res)