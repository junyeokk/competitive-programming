choices = {'c': 26, 'd': 10}
s = input()
MOD = 1_000_000_009
prev = ''

res = 1

for ch in s:
    if prev == ch:
        res *= choices[ch] - 1
    else:
        res *= choices[ch]
    prev = ch
    res %= MOD

print(res)