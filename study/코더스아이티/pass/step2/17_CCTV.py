menu = [['1000'], ['1010'], ['1100'], ['1110'], ['1111']]

for i in range(5):
    for j in range(1, 4):
        s = menu[i][0]
        menu[i].append(s[-j:] + s[:-j])

h, w = map(int, input().split())

def copy():
    global copyArr
    copyArr = []
    for i in range(h):
        t = arr[i].copy()
        copyArr.append(t)

arr = []
dr = []
for i in range(h):
    arr.append(list(map(int, input().split())))

for i in range(h):
    for j in range(w):
        if 1 <= arr[i][j] <= 5:
            dr.append([j, i, arr[i][j], 0])

def kill(x, y, dx, dy):
    x += dx
    y += dy
    while y >= 0 and y < h and x >= 0 and x < w:
        if copyArr[y][x] == 6:
            break
        copyArr[y][x] = 9
        x += dx
        y += dy

        

def solve():
    # 0: 왼쪽
    # 1: 위쪽
    # 2: 오른쪽
    # 3: 아래쪽
    copy()
    for d in dr:
        fd = menu[d[2] - 1][d[3]]
        x = d[0]
        y = d[1]
        if fd[0] == '1':
            kill(x, y, -1, 0)
        if fd[1] == '1':
            kill(x, y, 0, -1)
        if fd[2] == '1':
            kill(x, y, 1, 0)
        if fd[3] == '1':
            kill(x, y, 0, 1)
    cnt = 0
    for a in copyArr:
        for v in a:
            if v == 0:
                cnt += 1
    return cnt
    


ans = 64
def perm(idx):
    global ans
    if idx == len(dr):
        ans = min(ans, solve())
        return
    
    for i in range(4):
        dr[idx][3] = i
        perm(idx + 1)

perm(0)
print(ans)