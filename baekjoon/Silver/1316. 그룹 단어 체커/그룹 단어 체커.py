n = int(input())
cnt = 0

for i in range(n):
    alpha = []
    s = input()
    prev = ''
    for t in s:
        if prev == t:
            prev = t
            continue
        if t in alpha:
            break
        else:
            alpha.append(t)
            prev = t
    else:
        cnt += 1

print(cnt)
