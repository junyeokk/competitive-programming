n = int(input())
s = input() + '*'
d = {}

for c in range(26):
    d[chr(ord('A') + c)] = c + 1

idx = 27
w = ''
for c in s:
    if w + c in d:
        w += c
    else:
        print(d[w])
        d[w + c] = idx
        idx += 1
        w = c
