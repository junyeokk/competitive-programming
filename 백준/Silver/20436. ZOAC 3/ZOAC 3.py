# key_l = [
#     ['q', 'w', 'e', 'r', 't'], 
#     ['a', 's', 'd', 'f', 'g'], 
#     ['z', 'x', 'c', 'v', '']
# ]

# key_r = [
#     ['', 'y', 'u', 'i', 'o', 'p'],
#     ['', 'h', 'j', 'k', 'l', ''],
#     ['b', 'n', 'm', '', '', '']
# ]


sl, sr = map(str, input().split())
s = list(input())

pos = {}
res = 0

rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
left = set("qwertasdfgzxcv")
right = set("yuiophjklbnm")

for r, row in enumerate(rows):
    for c, ch in enumerate(row):
        pos[ch] = (r, c)

for ch in s:
    if ch in left:
        res += abs(pos[sl][0] - pos[ch][0]) + abs(pos[sl][1] - pos[ch][1]) + 1
        sl = ch
    elif ch in right:
        res += abs(pos[sr][0] - pos[ch][0]) + abs(pos[sr][1] - pos[ch][1]) + 1
        sr = ch

print(res)