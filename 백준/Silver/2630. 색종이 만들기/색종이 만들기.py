n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

white = 0
blue = 0

def solve(x, y, size):
    wcnt = 0
    bcnt = 0
    global white
    global blue
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j]:
                bcnt += 1
            else: 
                wcnt += 1
    if wcnt == size * size:
        white += 1
    elif bcnt == size * size:
        blue += 1
    else:
        solve(x, y, size // 2)
        solve(x + size // 2, y, size // 2)
        solve(x, y + size // 2, size // 2)
        solve(x + size // 2, y + size // 2, size // 2)

solve(0, 0, n)

print(white)
print(blue)
