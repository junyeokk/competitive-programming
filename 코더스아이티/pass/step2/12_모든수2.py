a, b = map(int, input().split())

card = []
for i in range(b):
    card.append(int(input()))

ans = [0 for i in range(a)]

def perm(idx):
    if idx == a:
        for i in range(a):
            print(card[ans[i]], end = ' ')
        print()
        return
    
    for i in range(b):
        ans[idx] = i
        perm(idx + 1)

perm(0)