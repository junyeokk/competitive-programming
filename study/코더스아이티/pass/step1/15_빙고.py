board = []

def remove(v):
    for i in range(5):
        for j in range(5):
            if board[i][j] == v:
                board[i][j] = -1

def check():
    # 가로 빙고
    for i in range(5):
        if board[i].count(-1) == 5:
            return True

    # 세로 빙고
    for i in range(5):
        cnt = 0
        for j in range(5):
            cnt += board[j][i]
        if cnt == -5:
            return True

    # 왼쪽 대각선 빙고
    cnt = 0
    for i in range(5):
        cnt += board[i][i]
        if cnt == -5:
            return True
    
    # 오른쪽 대각선 빙고
    cnt = 0
    for i in range(5):
        cnt += board[i][4-i]
        if cnt == -5:
            return True
    
    return False

for i in range(5):
    s = list(map(int, input().split()))
    board.append(s)

arr = list(map(int, input().split()))
for i in range(25):
    remove(arr[i])
    if check():
        print(i + 1)
        break
    

