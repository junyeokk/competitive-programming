n, m, x = map(int, input().split())
h = list(map(int, input().split()))
img = [['.'] * m for _ in range(n)]

# 산(#)
for i in range(m):
    h_m = h[i]
    for j in range(n - h_m, n):
        img[j][i] = '#'

# 교각(-), 터널(*)
for i in range(m):
    for j in range(n):
        if j == n - x:
            if img[j][i] == '#':
                img[j][i] = '*'
            else:
                img[j][i] = '-'
        if (i + 1) % 3 == 0 and j > n - x and img[j][i] != '#':
            img[j][i] = '|'

# print
for i in range(n):
    print(''.join(img[i]))