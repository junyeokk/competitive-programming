names = ['S', 'N', 'U']
best = -1
answer = ''

for i in range(3):
    price, weight = map(int, input().split())
    total = price * 10
    if total >= 5000:
        total -= 500
    ratio = weight * 10 / total
    if best < ratio:
        best = ratio
        answer = names[i]

print(answer)