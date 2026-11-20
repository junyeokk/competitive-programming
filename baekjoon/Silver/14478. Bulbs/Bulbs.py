t = int(input())

def solve():
    m, n = map(int, input().split())
    b = []
    rcnt = 0

    for i in range(m):
        s = list(map(int, input()))
        b.append(s)

    for i in range(m):
        for j in range(n):
            if b[i][n - j - 1] == 0:
                b[i][n - j - 1] = 1
                for k in range(i + 1, m): # 아래
                    b[k][n - j - 1] ^= 1
                for k in range(0, n - j - 1): # 왼쪽
                    b[i][k] ^= 1
                rcnt += 1
    print(rcnt)

for i in range(t):
    solve()
    