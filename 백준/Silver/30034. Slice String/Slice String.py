sp = set()

n = int(input())
for ch in input().split():
    sp.add(ch)

m = int(input())
for ch in input().split():
    sp.add(ch)

k = int(input())
for ch in input().split():
    sp.discard(ch)
sp.add(' ')

s = int(input())
ss = input()

piece = ''
for ch in ss:
    if ch in sp:
        if piece:
            print(piece)
        piece = ''
    else:
        piece += ch

if piece:
    print(piece)