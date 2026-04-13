c = 26
d = 10
s = list(input())
prev = ''

res = 1

for i in range(len(s)):
    if s[i] == 'c':
        if prev == s[i]:
            res *= c - 1
        else:
            res *= c
    elif s[i] == 'd':
        if prev == s[i]:
            res *= d - 1
        else:
            res *= d
    prev = s[i]
    res %= 1000000009

print(res)